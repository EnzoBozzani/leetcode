(() => {
	function largestAltitude(gain: number[]): number {
		let altitude = 0;
		let highest = 0;

		for (let i = 0; i < gain.length; i++) {
			altitude += gain[i];

			if (altitude > highest) {
				highest = altitude;
			}
		}

		return highest;
	}

	const examples = [
		[-5, 1, 5, 0, -7],
		[-4, -3, -2, -1, 4, 3, 2],
	];

	examples.forEach((e) => {
		console.log(e);
		console.log(largestAltitude(e));
		console.log();
	});
})();
