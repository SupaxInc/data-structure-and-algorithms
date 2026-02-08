export {};
const pacificAtlantic = (heights: number[][]): number[][] => {
    const ROWS = heights.length;
    const COLS = heights[0].length;
    const DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]];

    const pacific = new Set<string>();
    const atlantic = new Set<string>();

    const dfs = (row, col, ocean) => {
        if (ocean.has([row, col].toString())) return;

        ocean.add([row, col].toString());

        for (const [dx, dy] of DIRS) {
            const nr = row + dx;
            const nc = col + dy;

            if (nr < 0 || nc < 0 || nr > ROWS - 1 || nc > COLS - 1) continue;

            if (heights[nr][nc] >= heights[row][col]) {
                dfs(nr, nc, ocean);
            }
        }

        return;
    }

    for (let col = 0; col < COLS; col++) {
        dfs(0, col, pacific);
        dfs(ROWS - 1, col, atlantic);
    }

    for (let row = 0; row < ROWS; row++) {
        dfs(row, 0, pacific);
        dfs(row, COLS - 1, atlantic);
    }

    const res: number[][] = [];
    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            if (pacific.has([row, col].toString()) && atlantic.has([row, col].toString())) {
                res.push([row, col]);
            }
        }
    }

    return res;
};