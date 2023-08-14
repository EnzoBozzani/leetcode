function gcdOfStrings(str1: string, str2: string): string {
    const len = str1.length >= str2.length ? str1.length : str2.length;
    let str: string = '';
    for (let i: number = 0; i < len; i++){
        str += str1[i];

    }
    return str;
};