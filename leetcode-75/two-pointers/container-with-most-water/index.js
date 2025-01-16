(function () {
    function maxArea(height) {
        var min = function (a, b) { return (a < b ? a : b); };
        var max = 0;
        var pointer1 = 0;
        var pointer2 = height.length - 1;
        while (pointer1 < pointer2) {
            var area = min(height[pointer1], height[pointer2]) * (pointer2 - pointer1);
            if (area > max) {
                max = area;
            }
            if (height[pointer1] > height[pointer2]) {
                pointer2 -= 1;
            }
            else {
                pointer1 += 1;
            }
        }
        return max;
    }
    var examples = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
    ];
    examples.forEach(function (e) {
        console.log(e, maxArea(e));
    });
})();
