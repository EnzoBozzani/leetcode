(() => {
	function pivotIndex(nums: number[]): number {
		let lSum = 0;
		let rSum = 0;

		for (let i = 0; i < nums.length; i++) {
			if (i !== 0) {
				rSum += nums[i];
			}
		}

		if (lSum === rSum) {
			return 0;
		}

		for (let i = 0; i < nums.length - 1; i++) {
			lSum += nums[i];
			rSum -= nums[i + 1];

			if (lSum === rSum) {
				return i + 1;
			}
		}

		return -1;
	}

	const examples = [
		[1, 7, 3, 6, 5, 6],
		[1, 2, 3],
		[2, 1, -1],
	];

	examples.forEach((e) => {
		console.log(e);
		console.log(pivotIndex(e));
		console.log();
	});
})();
