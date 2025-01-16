(() => {
	function maxOperations(nums: number[], k: number): number {
		const sorted = nums.sort((a, b) => a - b);

		let left = 0;
		let right = sorted.length - 1;

		let operations = 0;

		while (left < right) {
			if (sorted[left] + sorted[right] === k) {
				operations += 1;
				left += 1;
				right -= 1;
			} else if (sorted[left] + sorted[right] < k) {
				left += 1;
			} else {
				right -= 1;
			}
		}

		return operations;
	}

	const examples: [number[], number][] = [
		[[1, 2, 3, 4], 5],
		[[3, 1, 3, 4, 3], 6],
	];

	examples.forEach((e) => {
		console.log(e[0], e[1]);
		console.log(maxOperations(e[0], e[1]));
		console.log();
	});
})();
