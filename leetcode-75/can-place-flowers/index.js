function canPlaceFlowers(flowerbed, n) {
    let freePlots = 0;
    flowerbed.forEach((plot, index) => {
        if (plot === 0 && flowerbed[index + 1] !== 1 && flowerbed[index - 1] !== 1) {
            freePlots++;
            flowerbed[index] = 1;
        }
    });
    return freePlots >= n;
}
;
