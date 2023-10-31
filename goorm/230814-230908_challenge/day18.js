const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
const input  = [];
rl.on('line', (line) => {
	input.push(line);
});

rl.on('close', () => {
	const [n, m] = input[0].split(" ").map(Number)
	const lines = input.slice(1,).map((el) => el.split(" ").map((el, idx) => {
		if (idx < 2) return Number(el)-1
		return el
	}))
	
	const arrayX = Array.from(Array(n), () => Array(n).fill(0));
	const arrayY = Array.from(Array(n), () => Array(n).fill(0));
	let result = 0;
	
	lines.forEach(line => {
		let [y, x, d] = line
		
		if (d === "L") {
			while (x >= 0) {
				arrayX[y][x] = (arrayX[y][x] || 0) + 1
				x--
			}
		} else if (d === "R") {
			while (x < n) {
				arrayX[y][x] = (arrayX[y][x] || 0) + 1
				x++
			}
		} else if (d === "U") {
			while (y >= 0) {
				arrayY[y][x] = (arrayY[y][x] || 0) + 1
				y--
			}
		} else if (d === "D") {
			while (y < n) {
				arrayY[y][x] = (arrayY[y][x] || 0) + 1
				y++
			}
		}
	})
	
	for (let i=0; i<n; i++) {
			for (let j=0; j<n; j++) {
				if (arrayY[i][j] && arrayX[i][j]) {
					result += arrayX[i][j] * arrayY[i][j]	
				}
			}
		}
	
	console.log(result)
})