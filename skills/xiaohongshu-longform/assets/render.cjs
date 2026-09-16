const { mkdir } = require("node:fs/promises");
const { resolve } = require("node:path");

function loadChromium() {
  const candidates = [process.env.PLAYWRIGHT_PATH, "playwright"].filter(Boolean);
  for (const candidate of candidates) {
    try {
      return require(candidate).chromium;
    } catch (_) {
      // Try the next known runtime.
    }
  }
  throw new Error("Playwright was not found. Load the workspace dependencies or install Playwright before rendering.");
}

const here = __dirname;
const outputDir = resolve(here, "output");

(async () => {
  await mkdir(outputDir, { recursive: true });
  const browser = await loadChromium().launch();
  const page = await browser.newPage({
    viewport: { width: 1080, height: 1440 },
    deviceScaleFactor: 1,
  });

  await page.goto(`file://${resolve(here, "index.html")}`, { waitUntil: "domcontentloaded" });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => Array.from(document.images).every((image) => image.complete));
  await page.waitForFunction(() => !window.MathJax || Boolean(document.querySelector("mjx-container")), { timeout: 15000 });

  const cards = page.locator(".poster");
  const count = await cards.count();
  const rendered = [];
  for (let index = 0; index < count; index += 1) {
    const number = String(index + 1).padStart(2, "0");
    const bytes = await cards.nth(index).screenshot({ path: resolve(outputDir, `${number}.png`) });
    rendered.push(bytes.toString("base64"));
  }

  const columns = Math.min(5, count);
  const rows = Math.ceil(count / columns);
  const thumbWidth = 270;
  const thumbHeight = 360;
  const gap = 24;
  const contactSheet = await browser.newPage({
    viewport: {
      width: columns * thumbWidth + (columns + 1) * gap,
      height: rows * thumbHeight + (rows + 1) * gap,
    },
  });
  await contactSheet.setContent(`
    <style>
      * { box-sizing: border-box; }
      html, body { margin: 0; background: #d8d6d0; }
      body { padding: ${gap}px; display: grid; grid-template-columns: repeat(${columns}, ${thumbWidth}px); gap: ${gap}px; }
      img { display: block; width: ${thumbWidth}px; height: ${thumbHeight}px; object-fit: contain; }
    </style>
    ${rendered.map((data) => `<img src="data:image/png;base64,${data}">`).join("")}
  `);
  await contactSheet.screenshot({ path: resolve(here, "preview-contact-sheet.png"), fullPage: true });

  await browser.close();
  console.log(`Rendered ${count} cards and preview-contact-sheet.png`);
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
