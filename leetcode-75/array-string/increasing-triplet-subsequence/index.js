function increasingTriplet(nums) {
    var first = Math.pow(2, 31) + 1;
    var second = Math.pow(2, 31) + 1;
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] <= first) {
            first = nums[i];
        }
        else if (nums[i] <= second) {
            second = nums[i];
        }
        else {
            return true;
        }
    }
    return false;
}
var examples = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 1, 5, 0, 4, 6],
];
examples.forEach(function (e) {
    console.log(e, increasingTriplet(e));
});
