var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
function compress(chars) {
    var s = '';
    var currentGroupLength = 1;
    var currentChar = chars[0];
    var sliceStart = 0;
    var initial = __spreadArray([], chars, true);
    initial.forEach(function (c, i) {
        if (i > 0) {
            if (c === currentChar) {
                currentGroupLength += 1;
            }
            else {
                if (currentGroupLength === 1) {
                    s += currentChar;
                }
                else {
                    s += currentChar;
                    s += currentGroupLength;
                }
                currentChar = c;
                currentGroupLength = 1;
                chars.splice.apply(chars, __spreadArray([sliceStart, i - sliceStart], s.split(''), false));
                sliceStart += s.length;
                s = '';
            }
            if (i + 1 === initial.length) {
                if (currentGroupLength === 1) {
                    s += currentChar;
                }
                else {
                    s += currentChar;
                    s += currentGroupLength;
                }
                chars.splice.apply(chars, __spreadArray([sliceStart, i + 1 - sliceStart], s.split(''), false));
            }
        }
    });
    if (s === '') {
        s = chars[0];
    }
    return chars.length;
}
function main() {
    var examples = [
        ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
        ['a'],
        ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
        ['a', 'a', 'a', 'b', 'b', 'a', 'a'],
    ];
    examples.forEach(function (e) {
        var temp = __spreadArray([], e, true);
        var len = compress(e);
        console.log(temp, len, e);
    });
}
main();
