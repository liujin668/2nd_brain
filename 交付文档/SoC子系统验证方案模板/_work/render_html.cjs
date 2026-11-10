const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require('C:/Users/jinliu01/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
  const root=path.resolve(__dirname,'..');
  const output=path.join(__dirname,'html_qa');fs.mkdirSync(output,{recursive:true});
  const browser=await chromium.launch({channel:"msedge",headless:true});
  const page=await browser.newPage({viewport:{width:1320,height:1000},deviceScaleFactor:1});
  await page.goto(pathToFileURL(path.join(root,'SoC子系统验证方案模板.html')).href);
  await page.evaluate(()=>document.fonts.ready);
  const audit=await page.evaluate(()=>({
    headings:[...document.querySelectorAll('h2,h3')].map(x=>x.textContent),
    tables:document.querySelectorAll('table').length,
    images:[...document.images].map(x=>({alt:x.alt,ok:x.complete&&x.naturalWidth>0})),
    overflow:document.documentElement.scrollWidth>window.innerWidth,
    chapters:[...document.querySelectorAll('section')].map(x=>({id:x.id,height:x.getBoundingClientRect().height}))
  }));
  for(const item of audit.chapters){
    const element=page.locator('#'+item.id);
    await element.screenshot({path:path.join(output,item.id+'.png')});
  }
  fs.writeFileSync(path.join(output,'audit.json'),JSON.stringify(audit,null,2));
  await browser.close();console.log(JSON.stringify(audit));
})().catch(e=>{console.error(e);process.exit(1)});
