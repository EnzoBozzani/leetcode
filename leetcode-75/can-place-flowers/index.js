function canPlaceFlowers(flowerbed, n) {
    let freePlots = 0;
    flowerbed.forEach((plot, index) => {
        const previous = flowerbed[index - 1];
        const next = flowerbed[index + 1];
        if (plot === 0 && next !== 1 && previous !== 1) {
            freePlots++;
            flowerbed[index] = 1;
        }
    });
    return freePlots >= n;
}
;
