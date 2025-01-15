(() => {
	/**
        Do not return anything, modify nums in-place instead.
    */
	function moveZeroes(nums: number[]): void {
		let pointer1 = 0;
		let pointer2 = 1;

		if (nums.length === 2 && nums[0] === 0) {
			nums[0] = nums[1];
			nums[1] = 0;
			return;
		}

		while (pointer2 < nums.length - 1) {
			while (nums[pointer1] !== 0) {
				pointer1 += 1;

				if (pointer1 === nums.length) return;
			}

			while (nums[pointer2] === 0 || pointer2 < pointer1) {
				pointer2 += 1;

				if (pointer2 === nums.length) return;
			}

			nums[pointer1] = nums[pointer2];
			nums[pointer2] = 0;

			while (nums[pointer1] !== 0) {
				pointer1 += 1;

				if (pointer1 === nums.length) return;
			}
		}
	}

	const examples = [[0, 1, 0, 3, 12], [0], [0, 0, 1], [1, 0, 1], [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]];

	examples.forEach((e) => {
		const temp = [...e];

		moveZeroes(e);

		console.log(temp, e);
	});
})();
