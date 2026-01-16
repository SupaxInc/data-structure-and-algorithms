const minEatingSpeed = (piles: number[], h: number): number => {
    let lo = 1;
    let hi = Math.max(...piles);

    let minK = hi;
    while (lo <= hi) {
        const midK = lo + Math.floor((hi - lo) / 2);

        let currH = 0;
        for (const p of piles) {
            currH += Math.ceil(p / midK);
        }

        if (currH <= h) {
            minK = Math.min(minK, midK);
            hi = midK - 1;
        } else {
            lo = midK + 1;
        }
    }

    return minK;
}