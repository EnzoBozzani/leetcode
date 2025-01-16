(() => {
	function maxArea(height: number[]): number {
		const min = (a: number, b: number) => (a < b ? a : b);

		let max = 0;

		let pointer1 = 0;
		let pointer2 = height.length - 1;

		while (pointer1 < pointer2) {
			const area = min(height[pointer1], height[pointer2]) * (pointer2 - pointer1);

			if (area > max) {
				max = area;
			}

			if (height[pointer1] > height[pointer2]) {
				pointer2 -= 1;
			} else {
				pointer1 += 1;
			}
		}

		return max;
	}

	const examples = [
		[1, 8, 6, 2, 5, 4, 8, 3, 7],
		[1, 1],
	];

	examples.forEach((e) => {
		console.log(e, maxArea(e));
	});
})();
