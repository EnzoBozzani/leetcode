function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let freePlots = 0;
    flowerbed.forEach((plot: number, index: number) => {
        if (plot === 0 && flowerbed[index + 1] !== 1 && flowerbed[index - 1] !== 1){
            freePlots++;
            flowerbed[index] = 1;
        }
    });
    return freePlots >= n;
};