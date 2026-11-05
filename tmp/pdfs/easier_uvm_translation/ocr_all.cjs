const fs = require('fs');
const path = require('path');
const {createWorker} = require('C:/Users/jinliu01/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/tesseract.js');
(async () => {
  const root = path.resolve('tmp/pdfs/easier_uvm_translation');
  const files = fs.readdirSync(root).filter(name=>/^source-\d\d\.png$/.test(name)).sort();
  let next=0;
  await Promise.all(Array.from({length:3}, async()=>{
    const worker=await createWorker('eng',1,{cachePath:root});
    while(next<files.length){
      const name=files[next++];
      const target=path.join(root,name.replace('source-','ocr-').replace('.png','.txt'));
      if(fs.existsSync(target))continue;
      const {data}=await worker.recognize(path.join(root,name));
      fs.writeFileSync(target,data.text,'utf8');
      console.log('OCR',name,'confidence',data.confidence);
    }
    await worker.terminate();
  }));
})().catch(e=>{console.error(e);process.exit(1)});