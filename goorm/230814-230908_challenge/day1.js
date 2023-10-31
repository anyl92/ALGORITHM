const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input;
rl.on('line', (line) => {
	input = line.split(" ");
	rl.close();
});

rl.on('close', () => {
	const weight = input[0]
	const repeat = input[1]
	const rmCalc = weight * (1 + (repeat / 30))
	const result = Math.floor(rmCalc)
	console.log(result)
})