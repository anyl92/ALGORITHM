// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		let result = 0;
		const items = [14, 7, 1];
		let value = line;
		for (let i=0; i<3; i++) {
			if (value / items[i] === 0) continue;
			result += Math.floor(value / items[i]);
			value = value % items[i]
		}
		console.log(result)
		rl.close();
	}
	
	process.exit();
})();
