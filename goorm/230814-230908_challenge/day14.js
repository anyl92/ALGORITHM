const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
const input = [];
const node = [];
rl.on('line', (line) => {
	input.push(line)
});

rl.on('close', () => {
	const [n, m, k] = input[0].split(" ").map(Number)
	const node = input.slice(1).map((el) => el.split(" ").map(Number))
	
	const map = {};
	node.forEach(([i, j]) => {
		!map[i] ? map[i] = [j] : map[i].push(j)
		!map[j] ? map[j] = [i] : map[j].push(i)
	})
	
	const memo = [];
	let cur = k;
	memo.push(cur);
	
	while (true) {
		if (!map[cur]) break;
		let next = map[cur].filter(el => !memo.includes(el)).sort((a, b) => a - b)[0];
		if (!next) break;
		memo.push(next);
		cur = next
	}
	
	console.log(memo.length, cur)
})
