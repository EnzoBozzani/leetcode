const isVowel = (char: string) => {
    char = char.toLowerCase();
    return char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u';
}

function reverseVowels(s: string): string {
    const str = s.split('');
    const vowels: string[] = [];
    for (let i = 0; i < str.length; i++){
        if (isVowel(str[i])){
            vowels.push(str[i]);
            str[i] = '';
        }
    }
    for (let i = 0; i < str.length; i++){
        if (str[i] === ''){
            str[i] = vowels[vowels.length - 1];
            vowels.pop();
        }
    }
    return str.join('');
};