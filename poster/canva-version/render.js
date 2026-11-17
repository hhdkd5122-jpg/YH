const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 3402, height: 5670 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve(__dirname, 'index.html'), { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  const h = await p.evaluate(() => ({page: document.querySelector('.page').scrollHeight, content: document.querySelector('footer').getBoundingClientRect().bottom}));
  console.log('page height', h);
  await p.pdf({ path: path.resolve(__dirname, 'Bergamot_Poster_90x150cm_CANVA.pdf'), width: '90cm', height: '150cm', printBackground: true, preferCSSPageSize: true, margin: {top:0,right:0,bottom:0,left:0} });
  await p.screenshot({ path: path.resolve(__dirname, 'preview.png'), fullPage: false });
  await b.close();
})();
