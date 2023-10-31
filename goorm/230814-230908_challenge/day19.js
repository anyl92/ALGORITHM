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
	const [n, m, s, e] = input[0].split(" ").map(Number);
	const nodes = input.slice(1,);
	const map = {};
	nodes.forEach((item) => {
		const [start, end] = item.split(" ").map(Number);
		map[start] = [...(map[start] || []), end]
		map[end] = [...(map[end] || []), start]
	})
	
	for (let day=1; day<=n; day++) {
		let dayCnt = 0;
		let flag = false;
		const visited = Array(n+1).fill(0);
		
		if (day === s || day === e) {
			console.log(-1)
			continue;
		}
		
		const q = [s];
		while (q.length) {
			dayCnt += 1;
			
			let fixedLength = q.length;
			for (let k=0; k<fixedLength; k++) {
				const cur = q.shift();
				visited[cur] = 1;
				
				map[cur].forEach((item) => {
					if (item === e) {
						flag = true;
						dayCnt += 1;
					} else if (item !== day && visited[item] === 0) {
						q.push(item);
					}
				})
				if (flag) break;
			}
			if (flag) break;
		}
		
		if (!flag) {
			dayCnt = -1;
		}
		console.log(dayCnt)
	}
})