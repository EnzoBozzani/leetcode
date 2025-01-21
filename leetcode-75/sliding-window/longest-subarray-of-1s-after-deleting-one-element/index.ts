(() => {
	function longestSubarray(nums: number[]): number {
		let max = 0;

		let diffK = 1;
		let start = 0;

		for (let end = 0; end < nums.length; end++) {
			if (nums[end] === 0) {
				if (diffK === 0) {
					if (nums[start] === 0) {
						start += 1;
					} else {
						while (nums[start] !== 0 && start < nums.length - 1) {
							start += 1;
						}

						start += 1;
					}
				} else {
					diffK -= 1;
				}
			}

			const size = end - start;

			if (size > max) {
				max = size;
			}
		}

		return max;
	}

	const examples = [
		[1, 1, 0, 1],
		[0, 1, 1, 1, 0, 1, 1, 0, 1],
		[1, 1, 1],
	];

	examples.forEach((e) => {
		console.log(e);
		console.log(longestSubarray(e));
		console.log();
	});
})();
