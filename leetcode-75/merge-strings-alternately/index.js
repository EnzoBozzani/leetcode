function mergeAlternately(word1, word2) {
    const len = word1.length >= word2.length ? word1.length : word2.length;
    let newString = '';
    for (let i = 0; i < len; i++) {
        if (word1[i]) {
            newString += word1[i];
        }
        if (word2[i]) {
            newString += word2[i];
        }
    }
    return newString;
}
;
mergeAlternately('abc', '123');
