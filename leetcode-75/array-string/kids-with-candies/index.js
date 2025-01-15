function kidsWithCandies(candies, extraCandies) {
    const highest = Math.max(...candies);
    const result = [];
    candies.forEach((candiesNumber, index) => {
        result[index] = candiesNumber + extraCandies >= highest;
    });
    return result;
}
;
console.log(kidsWithCandies([2, 3, 5, 1, 3], 3));
