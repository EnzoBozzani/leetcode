(() => {
	function isSubsequence(s: string, t: string): boolean {
		if (s.length > t.length) return false;

		let sPointer = 0;
		let tPointer = 0;

		while (sPointer < s.length) {
			while (t[tPointer] !== s[sPointer]) {
				tPointer += 1;

				if (tPointer === t.length) return false;
			}

			sPointer += 1;
			tPointer += 1;

			if (tPointer === t.length && sPointer !== s.length) return false;
		}

		return true;
	}

	const examples = [
		['abc', 'ahbgdc'],
		['axc', 'ahbgdc'],
		['c', 'b'],
		['acb', 'ahbgdc'],
		['abc', 'ahbgdc'],
	];

	examples.forEach((e) => {
		console.log(...e, isSubsequence(e[0], e[1]));
	});
})();
