const searchMatrix = (matrix: number[][], target: number): boolean => {
    if (matrix.length < 1) {
        return false;
    }

    const ROWS = matrix.length;
    const COLS = matrix[0].length;

    let lo = 0;
    let hi = ROWS * COLS - 1;

    while (lo <= hi) {
        const midIdx = lo + Math.floor((hi - lo) / 2);
        const midVal = matrix[Math.floor(midIdx / COLS)][midIdx % COLS];

        if (midVal === target) return true;

        if (midVal > target) {
            hi = midIdx - 1;
        } else {
            lo = midIdx + 1;
        }
    }

    return false;
};