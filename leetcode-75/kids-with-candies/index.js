function kidsWithCandies(candies, extraCandies) {
    let highest = 0;
    candies.forEach((candiesNumber) => {
        if (candiesNumber > highest) {
            highest = candiesNumber;
        }
    });
    console.log(highest);
    const result = [];
    candies.forEach((candiesNumber, index) => {
        if (candiesNumber + extraCandies >= highest) {
            result[index] = true;
        }
        else {
            result[index] = false;
        }
    });
    return result;
}
;
console.log(kidsWithCandies([2, 3, 5, 1, 3], 3));
