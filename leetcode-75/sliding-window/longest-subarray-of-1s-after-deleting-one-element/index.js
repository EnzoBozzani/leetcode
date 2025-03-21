(function () {
    function longestSubarray(nums) {
        var max = 0;
        var diffK = 1;
        var start = 0;
        for (var end = 0; end < nums.length; end++) {
            if (nums[end] === 0) {
                if (diffK === 0) {
                    if (nums[start] === 0) {
                        start += 1;
                    }
                    else {
                        while (nums[start] !== 0 && start < nums.length - 1) {
                            start += 1;
                        }
                        start += 1;
                    }
                }
                else {
                    diffK -= 1;
                }
            }
            var size = end - start;
            if (size > max) {
                max = size;
            }
        }
        return max;
    }
    var examples = [
        [1, 1, 0, 1],
        [0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1],
    ];
    examples.forEach(function (e) {
        console.log(e);
        console.log(longestSubarray(e));
        console.log();
    });
})();
