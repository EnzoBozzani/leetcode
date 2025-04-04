(() => {
	function longestOnes(nums: number[], k: number): number {
		let max = 0;

		if (k >= nums.length) return nums.length;

		let diffK = k;
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

			const size = end - start + 1;

			if (size > max) {
				max = size;
			}
		}

		return max;
	}

	const examples: [number[], number][] = [
		[[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2],
		[[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3],
		[[0, 0, 0, 1], 4],
		[[0, 0, 1, 1], 1],
	];

	examples.forEach((e) => {
		console.log(e[0], e[1]);
		console.log(longestOnes(e[0], e[1]));
		console.log();
	});
})();
