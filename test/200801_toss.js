// 1
function getMaskedName(name) {
    let ans = ''
    for (let i=0; i<name.length; i++) {
        if (i < 2) {
            ans += name[i]
        }
        else {
            ans += '*'
        }
    }
	return ans;
}
// console.log(getMaskedName('김수한무거북이와두루미삼천갑자동방삭'))

// 2
function splitDutchPayAmount(peopleCount, amount) {
    let calc = amount / peopleCount
    let result_list = []
    if (Number.isInteger(calc)) {
        for (let i=0; i<peopleCount; i++) {
            result_list.push(calc)
        }
    } else {
        calc = parseInt(calc)
        for (let i=0; i<peopleCount; i++) {
            result_list.push(calc)
        }
        let na = amount % peopleCount
        result_list[0] += na
    }
	return result_list;
}
// console.log(splitDutchPayAmount(3, 9850))

// 3
function commaizeNumber(num) {
    let ans = []
    let calc = 0
    while (num) {
        ans.push(num % 10)
        num = parseInt(num / 10)
        calc++
        if (calc % 3 == 0 && num) {
            ans.push(',')
        }
    }
    let res = ''
    for (i=ans.length-1; i>=0; i--) {
        res += ans[i]
    }
    return res;
}
// console.log(commaizeNumber(12342240))

// 4
function formatToKoreanNumber(num) {
    let hangle = ['', '', '', '', '만 ', '', '', '', '', '억 ']
    let ans = []
    let calc = 0
    while (num) {
        if (calc == 4 || calc == 9) {
            ans.push(hangle[calc])
            calc = 0
        }
        ans.push(num % 10)
        num = parseInt(num / 10)
        calc++
        if (calc % 3 == 0 && num) {
            ans.push(',')
        }
    }
    let res = ''
    for (i=ans.length-1; i>=0; i--) {
        res += ans[i]
    }
    if (res.includes('0,000')) {
        res = res.slice(0, -6)
    }
    return res;
}
console.log(formatToKoreanNumber(10000))

// 5
function getAge(birthDate, nowDate) {
    let comp = birthDate <= nowDate  // 만나이+1
    let age = nowDate.getYear() - birthDate.getYear() + 1
    let age2 = 0
    if (comp) {
        age2 = age - 1
    } else {
        age2 = age - 2
    }
    let ans = '만 ' + age2 + '세, 한국나이 ' + age1 + '세'
	return ans
}
// console.log(getAge())

function getAge(birthDate, nowDate) {
    let age = nowDate.getYear() - birthDate.getYear() + 1
    let age2 = 0
    
    if (Date('2020-08-31 00:00:00') === Date('2020-08-31 00:00:00')) {
        return true
        let ans = '만 ' + age2 + '세, 한국나이 ' + age + '세'
        return ans
    }
    // 생일 월이 지금 월보다 크다 생일 안지남
    if (birthDate.getMonth() > nowDate.getMonth()) {
        age2 = age - 2
        // 생일 월이랑 지금이랑 같다
    } else if (birthDate.getMonth() === nowDate.getMonth()) {
        // 생일 날짜가 지금 날짜보다 크다 아직 안지남
        if (birthDate.getDate() > nowDate.getDate()) {
            age2 = age - 2
            // 같거나 작다 오늘도 포함ㅎ서 생일 지남
        } else {
            age2 = age - 1
        } // 생일 월이 지금 월보다 작다 생일 지남
    } else {
        age2 = age - 1
    }
    let ans = '만 ' + age2 + '세, 한국나이 ' + age + '세'
    return ans
}

function test() {
    console.log(('2020-08-31 00:00:00' === '2020-08-31 00:00:00'))
    if ('2020-08-31 00:00:00' === '2020-08-31 00:00:00') {
        console.log('fff')
        return true
    }
}
// test()

function getAge(birthDate, nowDate) {
    let age = nowDate.getYear() - birthDate.getYear() + 1
    let age2 = 0
    
    if (nowDate === birthDate) {
        let ans = '만 ' + age2 + '세, 한국나이 ' + age + '세'
        return ans
    }
    
    if (birthDate.getMonth() > nowDate.getMonth()) {
        age2 = age - 2
    } else if (birthDate.getMonth() === nowDate.getMonth()) {
        if (birthDate.getDate() > nowDate.getDate()) {
            age2 = age - 2
        } else {
            age2 = age - 1
        } 
    } else {
        age2 = age - 1
    }
    let ans = '만 ' + age2 + '세, 한국나이 ' + age + '세'
    return ans
}