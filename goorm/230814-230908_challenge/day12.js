const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let N;
let result = 0;
const village = [];
rl.on('line', (line) => {
	if (N === undefined) {
		N = Number(line);
		return
	}
	if (village.length !== N) {
		village.push(line.split(" "));
		return;
	}
	
	rl.close();
});


rl.on('close', () => {
	const install = () => {
		while (queue.length) {
			let queuePop = queue.pop(0)
			let queueI = queuePop[0]
			let queueJ = queuePop[1]
			if (village[queueI][queueJ] === "1") {
				village[queueI][queueJ] = "0"
			}
			dir.map((d) => {
				nextI = queueI + d[0]
				nextJ = queueJ + d[1]
				if (nextI < 0 || nextI >= N || nextJ < 0 || nextJ >= N) return;
				if (village[nextI][nextJ] === "1") queue.push([nextI, nextJ]);
			})
		}
	}
	
	const queue = [];
	const dir = [[0, 1], [0, -1], [1, 0], [-1, 0]];
	for (let i=0; i<N; i++) {
		for (let j=0; j<N; j++) {
			if (village[i][j] === "1") {
				result++;
				queue.push([i, j]);
				install()
			}
		}
	}
	console.log(result)
})