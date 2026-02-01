export {};

import { Queue } from "@datastructures-js/queue";

const numIslandsDFS = (grid: string[][]): number => {
    const ROWS = grid.length;
    const COLS = grid[0].length;
    const DIRS: number[][] = [[0, 1], [1, 0], [-1, 0], [0, -1]];

    const dfs = (row, col) => {
        if (row < 0 || col < 0 || row > ROWS - 1 || col > COLS - 1) {
            return;
        }

        if (grid[row][col] === "0") {
            return;
        }

        grid[row][col] = "0";

        for (const [dx, dy] of DIRS) {
            dfs(row + dx, col + dy);
        }

        return;
    };

    let count = 0;
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (grid[r][c] === "1") {
                dfs(r, c);

                count += 1;
            }
        }
    }

    return count;
};

const numIslandsBFS = (grid: string[][]): number => { 
    const ROWS = grid.length;
    const COLS = grid[0].length;
    const DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]];
    
    const bfs = (row, col): void => {
        const queue = new Queue<[number, number]>([[row, col]]);

        while (!queue.isEmpty()) {
            const [r, c] = queue.dequeue();

            if (r < 0 || c < 0 || r > ROWS - 1 || c > COLS - 1) {
                continue;
            }

            if (grid[r][c] === "0") continue;

            grid[r][c] = "0";

            for (const [dx, dy] of DIRS) {
                queue.enqueue([r + dx, c + dy]);
            }
        }
    };

    let count = 0;
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (grid[r][c] === "1") {
                bfs(r, c);
                count += 1;
            }
        }
    }

    return count;
};