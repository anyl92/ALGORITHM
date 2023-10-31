const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input, N;
rl.on('line', (line) => {
	if(N === undefined) {
		N = line;
		return;
	}
	input = line;
	rl.close();
});

rl.on('close', () => {
	const set = new Set();
	for (let i=1; i<input.length; i++) {
		for (let j=i+1; j<input.length; j++) {
			set.add(input.slice(0, i));
			set.add(input.slice(i, j));
			set.add(input.slice(j));
		}
	}
	const sortedMap = new Map();
	const sortedList = [...set].sort();
	sortedList.map((el, idx) => {
		sortedMap.set(el, idx+1);
	})
	
	let totalsum;
	let result = 0;
	for (let i=1; i<input.length; i++) {
		for (let j=i+1; j<input.length; j++) {
			totalsum = sortedMap.get(input.slice(0, i)) + sortedMap.get(input.slice(i, j)) + sortedMap.get(input.slice(j))
			if (result < totalsum) result = totalsum;
		}
	}
	console.log(result)
})


