const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let N, input, A, B;
rl.on('line', (line) => {
	if (N === undefined) {
		N = Number(line);
		return
	}
	input = line.split(" ")
	A = Number(input[0])
	B = Number(input[1])
	rl.close();
});

rl.on('close', () => {
	let usedAMod = N % A;
	let usedBMod = N % B;
	let usedBCnt = Math.floor(N / B);
	let usedACnt;
	
	while (usedBCnt !== -1) {
		if (usedBMod % A === 0) {
			usedACnt = Math.floor(usedBMod / A)
			return console.log(usedACnt + usedBCnt)
		} else {
			usedBCnt--;
			usedBMod += B;
		}	
	}
	return console.log(-1)
})