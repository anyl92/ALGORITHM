const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input, N, K;
const village = [];
const memo = [];
const dir = [[1, 0], [-1, 0], [0, 1], [0, -1]];
const groups = Array(33).fill(0);

const BFS = (i, j, curNumber) => {
	let cnt = 1;
	const queue = [{r: i, c: j}];
	
	while (queue.length) {
		const {r, c} = queue.shift();

		dir.forEach((d) => {
			const nextI = r + d[0]
			const nextJ = c + d[1]
			if (nextI < 0 || nextJ < 0 || nextI >= N || nextJ >= N || memo[nextI][nextJ] === 1 || curNumber !== village[nextI][nextJ]) return;
			cnt++;
			queue.push({r:nextI, c:nextJ});
			memo[nextI][nextJ] = 1;
		});
	}
	if (cnt >= K) {
		groups[village[i][j]] += 1
	}
}

rl.on('line', (line) => {
	if (N === undefined) {
		const [n, k] = line.split(" ").map((el) => Number(el));
		N = n;
		K = k;
		return;
	}
	if (village.length < N) {
		const parsedLine = line.split(" ").map((el) => Number(el));
		const initLine = Array(parsedLine.lenght).fill(0);
		village.push(parsedLine);
		memo.push(initLine);
		if(village.length !== N) {
			return;
		}
	}
	rl.close();
});

rl.on('close', () => {
	for (let i=0; i<N; i++) {
		for (let j=0; j<N; j++) {
			if (memo[i][j] === 1) continue;
			memo[i][j] = 1;
			const cur = village[i][j];
			BFS(i, j, cur);
		}
	}
	
	let maxValue = 0;
	let result = 0;
	groups.forEach((el, idx) => {
		if (el < maxValue) return;
		maxValue = el;
		result = idx;
	})

	console.log(result)
})