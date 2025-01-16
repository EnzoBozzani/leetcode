(function () {
    function maxVowels(s, k) {
        var isVowel = function (char) { return char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u'; };
        var max = 0;
        var lastCurrent = 0;
        for (var i = 0; i < k; i++) {
            if (isVowel(s[i])) {
                lastCurrent += 1;
            }
        }
        if (s.length === k)
            return lastCurrent;
        max = lastCurrent;
        for (var i = 0; i < s.length; i++) {
            var current = lastCurrent;
            if (isVowel(s[i])) {
                current -= 1;
            }
            if (isVowel(s[i + k])) {
                current += 1;
            }
            if (current > max)
                max = current;
            lastCurrent = current;
        }
        return max;
    }
    var examples = [
        ['abciiidef', 3],
        ['aeiou', 2],
        ['leetcode', 3],
        ['ibpbhixfiouhdljnjfflpapptrxgcomvnb', 33],
    ];
    examples.forEach(function (e) {
        console.log(e[0], e[1]);
        console.log(maxVowels(e[0], e[1]));
        console.log();
    });
})();
