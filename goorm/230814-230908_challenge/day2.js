const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let n, h, m;
const minutes = [];
const setHM = (time, index) => {
	const parsedTime = Number(time);
	if(index === 0) {
		h = parsedTime;
		return;
	}
	m = parsedTime;
}

rl.on('line', (line) => {
	if(typeof n === 'undefined') {
		n = Number(line);
		return;
	} else if(typeof h === 'undefined') {
		line.split(' ').forEach(setHM);
		return;
	}
	minutes.push(Number(line));
	if(minutes.length === n) {
		rl.close();
	}
});

rl.on('close', () => {
	const basic = h*60 + m;
	const addition = minutes.reduce((acc, cur) => acc + cur, basic);
	const pureCalcTime = addition % 1440;
	if (pureCalcTime === 1440 || pureCalcTime === 0) {
		return console.log(0, 0)
	};
	const minute = pureCalcTime%60;
	const hour = (pureCalcTime - minute)/60;
	
	console.log(hour, minute)
})