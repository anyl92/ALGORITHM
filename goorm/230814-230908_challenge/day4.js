// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let n;
	let taste = [];
	let goodTaste = 0;
	let goodIndex = 0;
	let left, right;
	let result = 0;
	
	const main = (taste) => {
		taste.forEach((el, idx) => {
			if (goodTaste >= el) return;
			goodTaste = el;
			goodIndex = idx;
		})
		left = taste.slice(0, goodIndex).sort((a, b) => a-b);
		right = taste.slice(goodIndex).sort((a, b) => b-a);
		
		const sortedList = [...left, ...right];
		
		if (sortedList.length !== taste.length) {
			result = 0
			return;
		}
		for (let i=0; i<taste.length; i++) {
			if (taste[i] !== sortedList[i]) {
				result = 0
				return;
			} else {
				result += taste[i]
			}
		}
		return;
	}
	
	for await (const line of rl) {
		if (n === undefined) {
			n = Number(line);
		} else {
			taste = [line];
			main(taste[0].split(" ").map(Number));
			console.log(result)
		}
	}
	rl.close();
	process.exit();
})();
