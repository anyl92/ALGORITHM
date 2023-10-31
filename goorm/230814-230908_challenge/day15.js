const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

let lines = [];
let N, K;
let P = [];
let C = [];
let ans = 0;

rl.on('line', (line) => {
	lines.push(line.trim());
});

rl.on('close', () => {
	[N, K] = lines[0].split(' ').map(Number);
	P[0] = 0;
	C[0] = 0;

	for (let i = 1; i <= N; i++) {
		[P[i], C[i]] = lines[i].split(' ').map(Number);
	}

	const slices = {}
	for (let i=1; i<=N; i++) {
		const sliceValue = C[i] / P[i]
		if (slices[sliceValue]) {
			slices[sliceValue].push(P[i])
		} else {
			slices[sliceValue] = [P[i]]
		}
	}
	
	let result = 0;
	const sortedFruits = Object.entries(slices).sort((a, b) => b[0] - a[0]);
	for (let i=0; i<sortedFruits.length; i++) {
		const fullness = sortedFruits[i][0]
		const prices = sortedFruits[i][1]
		const fruitPrices = prices.sort((a, b) => b-a);
		for (let j=0; j<fruitPrices.length; j++) {
			const canUse = fruitPrices[j]
			if (K < canUse) {
				result += fullness * K
				K -= K
				console.log(result)
				return;
			}
			result += fullness * canUse
			K -= canUse
		}
	}
	console.log(result)
});