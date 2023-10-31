const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
const input = []
rl.on('line', (line) => {
	input.push(line);
});

rl.on('close', () => {
	const [n, k] = input[0].split(" ").map(Number)
	const numbers = input.slice(1)[0].split(" ").map(Number)
	
	const oneCntList = numbers.map((el, idx) => {
		const binNum = el.toString(2)
		let cnt = 0;
		binNum.split("").forEach(bin => {
			if (bin === '1') cnt++;
		})
		return [cnt, numbers[idx]]
	})
	
	const sortedNumbers = oneCntList.sort((a, b) => {
		if (a[0] === b[0]) {
			return b[1] - a[1]
		}
		return b[0] - a[0]
	})
	console.log(sortedNumbers[k-1][1])
})