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
    /**
        Do not return anything, modify nums in-place instead.
    */
    function moveZeroes(nums) {
        var pointer1 = 0;
        var pointer2 = 1;
        if (nums.length === 2 && nums[0] === 0) {
            nums[0] = nums[1];
            nums[1] = 0;
            return;
        }
        while (pointer2 < nums.length - 1) {
            while (nums[pointer1] !== 0) {
                pointer1 += 1;
                if (pointer1 === nums.length)
                    return;
            }
            while (nums[pointer2] === 0 || pointer2 < pointer1) {
                pointer2 += 1;
                if (pointer2 === nums.length)
                    return;
            }
            nums[pointer1] = nums[pointer2];
            nums[pointer2] = 0;
            while (nums[pointer1] !== 0) {
                pointer1 += 1;
                if (pointer1 === nums.length)
                    return;
            }
        }
    }
    var examples = [[0, 1, 0, 3, 12], [0], [0, 0, 1], [1, 0, 1], [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]];
    examples.forEach(function (e) {
        var temp = __spreadArray([], e, true);
        moveZeroes(e);
        console.log(temp, e);
    });
})();
