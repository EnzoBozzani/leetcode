var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
(function () {
    function isSubsequence(s, t) {
        if (s.length > t.length)
            return false;
        var sPointer = 0;
        var tPointer = 0;
        while (sPointer < s.length) {
            while (t[tPointer] !== s[sPointer]) {
                tPointer += 1;
                if (tPointer === t.length)
                    return false;
            }
            sPointer += 1;
            tPointer += 1;
            if (tPointer === t.length && sPointer !== s.length)
                return false;
        }
        return true;
    }
    var examples = [
        ['abc', 'ahbgdc'],
        ['axc', 'ahbgdc'],
        ['c', 'b'],
        ['acb', 'ahbgdc'],
        ['abc', 'ahbgdc'],
    ];
    examples.forEach(function (e) {
        console.log.apply(console, __spreadArray(__spreadArray([], e, false), [isSubsequence(e[0], e[1])], false));
    });
})();
