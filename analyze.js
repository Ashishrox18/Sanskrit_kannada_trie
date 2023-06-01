const fs = require('fs');
const Aksharas = require("@vipran/aksharas").default;



// Read input file
fs.readFile('./kannadaexcel/uniqsansk.txt', 'utf8', (err, input) => {
  if (err) {
    console.error(`Error reading input file: ${err}`);
    return;
  }

  // Analyze aksharas
  const results = Aksharas.analyse(input);
  const aksharas = results.aksharas.map((akshara) => akshara.value);

  // Prepare output string
  const output = aksharas.join('\n');

  // Write to output file
  fs.writeFile('./kannadaexcel/sansletspin.txt', output, 'utf8', (err) => {
    if (err) {
      console.error(`Error writing to output file: ${err}`);
      return;
    }
    console.log(`Output file created successfully.`);
  });
});
