function reverseWords(s) {
    const words = s.split(' ');
    let strArr = [];
    for (let i = words.length - 1; i >= 0; i--) {
        if (words[i] !== '') {
            strArr.push(words[i]);
        }
    }
    return strArr.join(' ');
}
;
console.log(reverseWords(' My name    is Enzo '));
