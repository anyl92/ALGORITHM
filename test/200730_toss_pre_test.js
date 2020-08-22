// 1
function printAgeGroup(age) {
    let set = parseInt(age / 10)
    if (set === 0) {
        return '10대 미만';
    }
    else if (set > 8) {
	    return '90대 이상';
    }
    else {
        return set + '0대'
    }
}
console.log(printAgeGroup(33))

// 2
function getAmount(text) {
    let ans = ''
	for (let i=0; i<text.length; i++) {
        if (Number(text[i])) {
            ans += text[i]
        } else if (text[i] == '0') {
            ans += text[i]
        }
    }
	return Number(ans);
}
console.log(getAmount('$1,250'))

// 3
function calculate(type, operands) {
    if (type === 'add') {
        let tmp = 0
        operands.forEach(e => {
            tmp += e
        });
        return tmp;
    }
    else {
        let tmp = 1
        operands.forEach(e => {
            tmp *= e
        });
        return tmp;
    }
}
console.log(calculate("add", [1, 2]))