(() => {
	function compress(chars: string[]): number {
		let s = '';
		let currentGroupLength = 1;
		let currentChar = chars[0];
		let sliceStart = 0;

		const initial = [...chars];

		initial.forEach((c, i) => {
			if (i > 0) {
				if (c === currentChar) {
					currentGroupLength += 1;
				} else {
					if (currentGroupLength === 1) {
						s += currentChar;
					} else {
						s += currentChar;
						s += currentGroupLength;
					}

					currentChar = c;
					currentGroupLength = 1;

					chars.splice(sliceStart, i - sliceStart, ...s.split(''));

					sliceStart += s.length;
					s = '';
				}

				if (i + 1 === initial.length) {
					if (currentGroupLength === 1) {
						s += currentChar;
					} else {
						s += currentChar;
						s += currentGroupLength;
					}

					chars.splice(sliceStart, i + 1 - sliceStart, ...s.split(''));
				}
			}
		});

		if (s === '') {
			s = chars[0];
		}

		return chars.length;
	}

	const examples = [
		['a', 'a', 'b', 'b', 'c', 'c', 'c'],
		['a'],
		['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
		['a', 'a', 'a', 'b', 'b', 'a', 'a'],
	];

	examples.forEach((e) => {
		const temp = [...e];
		const len = compress(e);
		console.log(temp, len, e);
	});
})();
