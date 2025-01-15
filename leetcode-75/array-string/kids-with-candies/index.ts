function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const highest: number = Math.max(...candies);
    const result: boolean[] = [];
    candies.forEach((candiesNumber: number, index: number) => {
        result[index] = candiesNumber + extraCandies >= highest;
    })
    return result;
};

console.log(kidsWithCandies([2,3,5,1,3], 3));
