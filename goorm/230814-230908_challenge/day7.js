const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input, N, K
const cloudList = [];
rl.on('line', (line) => {
	if (N === undefined) {
		input = line.split(" ");
		N = input[0]
		K = input[1]
		return
	}
	if (cloudList.length !== N) {
		cloudList.push(line.split(" "));
		return
	}
	rl.close();
});

rl.on('close', () => {
	let result = 0;
	const direction = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]];
	for (let i=0; i<N; i++) {
		for (let j=0; j<N; j++) {
			if (cloudList[i][j] === '1') continue;
			let cloudCnt = 0
			direction.map((d) => {
				nextI = i + d[0]
				nextJ = j + d[1]
				if (nextI >= 0 && nextI < N && nextJ >= 0 && nextJ < N) {
					if (cloudList[nextI][nextJ] === "1") cloudCnt++;
				}
			})
			if (cloudCnt === Number(K)) result++;
		}
	}
	console.log(result)
})