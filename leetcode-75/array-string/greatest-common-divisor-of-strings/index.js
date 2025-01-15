function multiplyString(str, times) {
    let result = "";
    for (let i = 0; i < times; i++) {
        result += str;
    }
    return result;
}
function gcdOfStrings(str1, str2) {
    let result = "";
    let multiplier1;
    let multiplier2;
    let multipliedGCD1 = "";
    let multipliedGCD2 = "";
    for (let i = 1; i <= str2.length; i++) {
        let GCD = "";
        GCD = str2.substring(0, i);
        if ((str1.length % GCD.length === 0) && (str2.length % GCD.length === 0)) {
            multiplier1 = str1.length / GCD.length;
            multiplier2 = str2.length / GCD.length;
            multipliedGCD1 = multiplyString(GCD, multiplier1);
            multipliedGCD2 = multiplyString(GCD, multiplier2);
            (multipliedGCD1 === str1) && (multipliedGCD2 === str2) ? (result = GCD) : null;
        }
    }
    return result;
}
