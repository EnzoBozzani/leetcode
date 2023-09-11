function reverseWords(s) {
    const words = s.split(' ');
    let strArr = [];
    for (let i = words.length - 1; i >= 0; i--) {
        if (words[i] !== '') {
            strArr.push(words[i]);
        }
    }
    console.table(strArr);
    while (strArr.includes('')) {
        let i;
        for (i = 0; i < strArr.length; i++) {
            if (strArr[i] === '') {
                break;
            }
        }
        strArr.splice(i, 1);
    }
    return strArr.join(' ');
}
;
console.log(reverseWords(' My name    is Enzo '));
