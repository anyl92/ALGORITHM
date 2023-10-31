const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
const input = [];
rl.on('line', (line) => {
	input.push(line);
});

rl.on('close', () => {
	const n = Number(input[0]);
	const goormS = input[1].split(" ").map(el => Number(el-1));
	const playerS = input[2].split(" ").map(el => Number(el-1));
	const fields = input.slice(3).map(el => el.split(" "));
	const dir = {R: [0, 1], L: [0, -1], U: [-1, 0], D: [1, 0]}
	
	const play = (queue, memo) => {
		let moveCnt = 1;
		
		while (queue.length) {
			let [r, c] = queue.shift();
			memo[r][c] = 1;
			const cur = fields[r][c];
			const direction = cur.substr(-1);
			let playCnt = Number(cur.slice(0, -1));

			let nr = r, nc = c;
			while (playCnt > 0) {
				nr += dir[direction][0];
				nc += dir[direction][1];
				if (nr >= n) { nr = 0 }
				if (nr < 0) { nr = n-1 }
				if (nc >= n) { nc = 0 }
				if (nc < 0) { nc = n-1 };
				if (memo[nr][nc] === 1) {
					queue.length = 0;
					return moveCnt
				}
				memo[nr][nc] = 1;
				moveCnt++;
				playCnt--;
			}
			memo[nr][nc] = 1;
			queue.push([nr, nc]);
		}
		return moveCnt
	}
	
	const goormMemo = Array.from(Array(n), () => Array(n).fill(0));
	const goormResult = play([goormS], goormMemo)
	
	const playerMemo = Array.from(Array(n), () => Array(n).fill(0));
	const playerResult = play([playerS], playerMemo)
	
	if (goormResult > playerResult) {
		console.log("goorm", goormResult)
	} else {
		console.log("player", playerResult)	
	}
})