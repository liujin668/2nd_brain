const fs = require('fs');
const path = require('path');
const {createWorker} = require('C:/Users/jinliu01/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/tesseract.js');
(async () => {
  const work = path.resolve('tmp/pdfs/easier_uvm_translation');
  const worker = await createWorker('eng', 1, {cachePath: work});
  const result = await worker.recognize(path.join(work,'source-01.png'));
  fs.writeFileSync(path.join(work,'ocr-01.txt'),result.data.text,'utf8');
  console.log(result.data.text.slice(0,3000));
  await worker.terminate();
})().catch(error => { console.error(error); process.exit(1); });