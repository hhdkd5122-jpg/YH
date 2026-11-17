// Render poster.html to a 900 x 1500 mm PDF and a PNG preview.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const dir = __dirname;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1700, height: 2834 } });
  await page.goto('file://' + path.join(dir, 'poster.html'), { waitUntil: 'networkidle' });
  await page.waitForTimeout(800);

  // overflow report: anything taller than the canvas
  const report = await page.evaluate(() => {
    const p = document.querySelector('.poster');
    const out = { posterHeight: p.getBoundingClientRect().height, bodyScroll: document.body.scrollHeight, overflow: [] };
    document.querySelectorAll('.card, .band1, .band2, .ev1, .ev2, .method, .hypo, .plate').forEach(el => {
      if (el.scrollHeight > el.clientHeight + 2) {
        out.overflow.push({ cls: el.className, scroll: el.scrollHeight, client: el.clientHeight });
      }
    });
    const sheet = document.querySelector('.sheet').getBoundingClientRect();
    out.contentBottom = sheet.bottom;
    return out;
  });
  console.log(JSON.stringify(report, null, 2));

  await page.pdf({
    path: path.join(dir, 'Bergamot_Poster_90x150cm.pdf'),
    width: '900mm', height: '1500mm',
    printBackground: true, pageRanges: '1'
  });

  await page.screenshot({ path: path.join(dir, 'preview.png'), fullPage: true, scale: 'css' });
  await browser.close();
  console.log('done');
})();
