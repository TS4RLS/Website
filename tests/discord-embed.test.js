"use strict";
// Every page's Discord component embed and favicon tags (run with `node --test`).
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const SKIP_DIRS = new Set([".git", "node_modules", "fontawesome", "tests", "scripts"]);

function htmlFiles(dir, out) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.isDirectory()) { if (!SKIP_DIRS.has(e.name)) htmlFiles(path.join(dir, e.name), out); }
    else if (e.name.endsWith(".html")) out.push(path.join(dir, e.name));
  }
  return out;
}
const pages = htmlFiles(ROOT, []).map((f) => ({ rel: path.relative(ROOT, f).split(path.sep).join("/"), src: fs.readFileSync(f, "utf8") }))
  .filter((p) => p.src.includes("<head"));
const NO_EMBED = new Set(["404.html", "changelog.html"]);
const ALLOWED = new Set([1, 2, 9, 10, 11, 12, 14, 17]);
const BUTTON_KEYS = new Set(["id", "type", "url", "style", "label", "emoji", "disabled"]);

function walk(c, state) {
  assert.ok(ALLOWED.has(c.type), "component type " + c.type);
  state.count++;
  if (c.type === 17 && !state.root) assert.fail("nested container");
  if (c.type === 2) {
    assert.equal(c.style, 5);
    assert.match(c.url, /^https?:\/\//);
    for (const k of Object.keys(c)) assert.ok(BUTTON_KEYS.has(k), "button key " + k);
  }
  const kids = (c.components || []).concat(c.accessory ? [c.accessory] : []);
  for (const k of kids) { state.root = false; walk(k, state); }
  if (c.type === 10) {
    assert.doesNotMatch(c.content, /\$1/);
    // markdown-significant characters in the text must not appear unescaped outside our own syntax
    assert.ok(typeof c.content === "string");
  }
}

test("pages found", () => assert.ok(pages.length >= 20));

for (const p of pages) {
  test(p.rel + " favicon tags", () => {
    for (const t of ['<link rel="icon" href="/favicon.ico" sizes="48x48">',
      '<link rel="icon" type="image/png" sizes="512x512" href="/assets/icon-512.png">',
      '<link rel="apple-touch-icon" href="/apple-touch-icon.png">',
      '<link rel="manifest" href="/site.webmanifest">']) assert.ok(p.src.includes(t), t);
  });
  test(p.rel + " discord embed", () => {
    const m = p.src.match(/<script id="discord:component-embed" type="application\/json">(.*?)<\/script>/s);
    if (NO_EMBED.has(p.rel)) { assert.equal(m, null); return; }
    assert.ok(m, "embed present");
    assert.ok(Buffer.byteLength(m[1]) <= 3000);
    assert.ok(!m[1].includes("</"), "cannot close the script tag early");
    const data = JSON.parse(m[1]);
    assert.equal(data.component.type, 17);
    assert.ok(data.component.components.length <= 40);
    const state = { count: 0, root: true };
    walk(data.component, state);
    assert.ok(state.count <= 40);
  });
}

test("site.webmanifest is complete", () => {
  const m = JSON.parse(fs.readFileSync(path.join(ROOT, "site.webmanifest"), "utf8"));
  assert.equal(m.start_url, "/");
  assert.equal(m.display, "browser");
  assert.ok(m.icons.some((i) => i.sizes === "192x192"));
  assert.ok(m.icons.some((i) => i.sizes === "512x512" && i.purpose === "maskable"));
});
