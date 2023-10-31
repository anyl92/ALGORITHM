const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
const input = [];
rl.on('line', (line) => {
	input.push(line);
});
const l = console.log;

rl.on('close', () => {
	const [n, m] = input[0].split(' ').map(Number);
	const map = {};
	const check = Array.from(Array(n + 1), () => Array(n + 1).fill(0));
	const memo = Array(n + 1).fill(0);
	
	input.slice(1).forEach(line => {
		const [s, e] = line.split(' ').map(Number);
		map[s] = [...(map[s] || []), e];
		check[s][e] = 1;
	});
	
	const bfs = (i) => {
		const q = [i];
		memo[i] = 1;
		
		while(q.length) {
			const cur = q.shift();
			if(!map[cur]) break;
			
			for(const next of map[cur]) {
				if(!check[next][cur] || memo[next]) continue;
				memo[next] = 1;
				q.push(next);
			}
		}
	}
	
	let answer = 0;
	for(let i = 1; i <= n; i++) {
		if(memo[i]) continue;
		bfs(i);
		answer++;
	}
	l(answer);
});


//unionfind

// const readline = require('readline');
// let rl = readline.createInterface({
// 	input: process.stdin,
// 	output: process.stdout,
// });
// const input = [];
// rl.on('line', (line) => {
// 	input.push(line);
// }); 

// const find = (parent, cur) => {
// 	if(parent[cur] === cur) return cur;
// 	parent[cur] = find(parent, parent[cur]);
// 	return parent[cur];
// }

// const union = (parent, a, b) => {
// 	const aRoot = find(parent, a);
// 	const bRoot = find(parent, b);
// 	if(aRoot === bRoot) return;
// 	const value = Math.min(aRoot, bRoot);
// 	parent[Math.max(aRoot, bRoot)] = value;
// }

// rl.on('close', () => {
// 	const [n, m] = input[0].split(" ").map(Number);
// 	const graphMap = Array(n+1).fill(0).map(el => Array(n+1).fill(0));
// 	const graph = {};
// 	input.slice(1).forEach((el) => {
// 		const [s, e] = el.split(" ").map(Number);
// 		graphMap[s][e] = 1;
// 		graph[s] = [...(graph[s] || []), e];
// 	})
// 	const parent = Array(n+1).fill(0).map((_, idx) => idx);
	
// 	for (let i=1; i<=n; i++) {
// 		if (!graph[i]) continue;
// 		for (const j of graph[i]) {
// 			if (!graphMap[j][i]) continue;
// 			union(parent, i, j);
// 		}
// 	}
	
// 	const answer = new Set();
// 	for(let i=1; i<=n; i++) {
// 		answer.add(find(parent, i));
// 	}
// 	console.log(answer.size);
// }) 