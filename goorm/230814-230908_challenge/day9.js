const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input, N, K
let result = 0
const landList = []
const bombList = []

rl.on('line', (line) => {
	if (N === undefined) {
		input = line.split(" ");
		N = input[0]
		K = input[1]
		return;
	}
	if (N) {
		landList.push(line.split(" "))
		N -= 1
		return;
	} 
	if (K) {
		bombList.push(line.split(" "))
		K -= 1
		return;
	}
	rl.close();
});

rl.on('close', () => {
	const direction = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]];
	
	for (let i=0; i<input[0]; i++) {
		for (let j=0; j<input[0]; j++) {
			if (landList[i][j] === "@") continue;
			if (landList[i][j] === "#") continue;
			landList[i][j] = Number(landList[i][j])
		}
	}

	bombList.map((bomb) => {
		bomb = [Number(bomb[0]), Number(bomb[1])]
		direction.map((d) => {
			nextI = bomb[0]-1 + d[0];
			nextJ = bomb[1]-1 + d[1];
			if (nextI < 0 || nextI >= input[0] || nextJ < 0 || nextJ >= input[0]) return;
			if (landList[nextI][nextJ] === "#") return;
			
			if (landList[nextI][nextJ] === "@") {
				landList[nextI][nextJ] = -2
			} else if (landList[nextI][nextJ] < 0) {
				landList[nextI][nextJ] -= 2
			} else {
				landList[nextI][nextJ] += 1
			}
			
			if (result < Math.abs(landList[nextI][nextJ])) {
					result = Math.abs(landList[nextI][nextJ])
				}
		})
	})
	
	console.log(result)
})