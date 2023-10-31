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
	const [n, k, q] = input[0].split(" ").map(Number);
	const array = input.slice(1, n+1).map((item) => item.split(""));
	const words = input.slice(n+1,).map((item) => item.split(" ").map((item, idx) => {
		if (idx < 2) {
			return Number(item)-1
		} else {
			return item
		}
	}));
	const dir = [[0, 1], [1, 0], [0, -1], [-1, 0]];
	
	words.forEach(([y, x, c]) => {
		array[y][x] = c;
		const visited = Array(n).fill(0).map((item) => Array(n).fill(0));
		const memo = [[y, x]];
		let cnt = 1;
		
		const queue = [[y, x]];
		visited[y][x] = 1;
		
		while (queue.length) {
			const [y, x] = queue.shift();
			dir.forEach(([dy, dx]) => {
				dy += y
				dx += x
				if (dy < n && dy >= 0 && dx < n && dx >= 0 && !visited[dy][dx]) {
					if (array[dy][dx] === c) {
						queue.push([dy, dx]);
						memo.push([dy, dx]);
						visited[dy][dx] = 1;
						cnt++;
					}
				}
			})
		}
		
		if (cnt >= k) {
			memo.forEach(([y, x]) => {
				array[y][x] = ".";
			})
		}
	})
	console.log(array.map(item => item.join("")).join("\n"))
})