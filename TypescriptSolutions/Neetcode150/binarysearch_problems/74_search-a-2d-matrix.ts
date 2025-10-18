const searchMatrix = (matrix: number[][], target: number): boolean => {
    const ROWS = matrix.length, COLS = matrix[0].length;

    let lo = 0, hi = ROWS * COLS - 1;
    
    while (lo <= hi) {
        const mid = lo + Math.floor((hi - lo)/2);

        const midVal = matrix[Math.floor(mid / COLS)][mid % COLS];

        if (midVal === target) {
            return true;
        } else if (midVal > target) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }

    return false;
}