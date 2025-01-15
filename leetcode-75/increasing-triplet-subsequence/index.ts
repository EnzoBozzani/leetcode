function increasingTriplet(nums: number[]): boolean {
	let first = 2 ** 31 + 1;
	let second = 2 ** 31 + 1;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] <= first) {
			first = nums[i];
		} else if (nums[i] <= second) {
			second = nums[i];
		} else {
			return true;
		}
	}

	return false;
}

const examples = [
	[1, 2, 3, 4, 5],
	[5, 4, 3, 2, 1],
	[2, 1, 5, 0, 4, 6],
];

examples.forEach((e) => {
	console.log(e, increasingTriplet(e));
});
