(function () {
    function maxOperations(nums, k) {
        var sorted = nums.sort(function (a, b) { return a - b; });
        var left = 0;
        var right = sorted.length - 1;
        var operations = 0;
        while (left < right) {
            if (sorted[left] + sorted[right] === k) {
                operations += 1;
                left += 1;
                right -= 1;
            }
            else if (sorted[left] + sorted[right] < k) {
                left += 1;
            }
            else {
                right -= 1;
            }
        }
        return operations;
    }
    var examples = [
        [[1, 2, 3, 4], 5],
        [[3, 1, 3, 4, 3], 6],
    ];
    examples.forEach(function (e) {
        console.log(e[0], e[1]);
        console.log(maxOperations(e[0], e[1]));
        console.log();
    });
})();
