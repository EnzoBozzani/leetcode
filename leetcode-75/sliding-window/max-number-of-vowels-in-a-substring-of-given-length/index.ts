(() => {
	function maxVowels(s: string, k: number): number {
		const isVowel = (char: string) => char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u';

		let max = 0;

		let lastCurrent = 0;

		for (let i = 0; i < k; i++) {
			if (isVowel(s[i])) {
				lastCurrent += 1;
			}
		}

		if (s.length === k) return lastCurrent;

		max = lastCurrent;

		for (let i = 0; i < s.length; i++) {
			let current = lastCurrent;

			if (isVowel(s[i])) {
				current -= 1;
			}

			if (isVowel(s[i + k])) {
				current += 1;
			}

			if (current > max) max = current;

			lastCurrent = current;
		}

		return max;
	}

	const examples: [string, number][] = [
		['abciiidef', 3],
		['aeiou', 2],
		['leetcode', 3],
		['ibpbhixfiouhdljnjfflpapptrxgcomvnb', 33],
	];

	examples.forEach((e) => {
		console.log(e[0], e[1]);
		console.log(maxVowels(e[0], e[1]));
		console.log();
	});
})();
