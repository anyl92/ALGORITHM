const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let n;
let T = [];
rl.on('line', (line) => {
	if (n === undefined) {
		n = line;
	} else if (T.length !== n) {
		T.push(line)
	} else {
		rl.close();	
	}
});

rl.on('close', () => {
	const result = T.reduce((acc, cur) => {
		acc += Math.floor(eval(cur));
		return acc
	}, 0)
	console.log(result)
})