export {};

import { Queue } from "@datastructures-js/queue";
const maxAreaOfIslandDFS = (grid: number[][]): number => {
    const ROWS = grid.length;
    const COLS = grid[0].length;
    const DIRS =  [[0, 1], [1, 0], [-1, 0], [0, -1]];

    const dfs = (row, col) => {
        if (row < 0 || col < 0 || row > ROWS - 1 || col > COLS - 1) return 0;
        if (grid[row][col] === 0) return 0;

        grid[row][col] = 0;
        let area = 1;

        for (const [dx, dy] of DIRS) {
            area += dfs(row + dx, col + dy);
        }

        return area;
    }

    let maxArea = 0;
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (grid[r][c] === 1) {
                let area = dfs(r, c);
                maxArea = Math.max(maxArea, area);
            }
        }
    }

    return maxArea;
};

const maxAreaOfIslandBFS = (grid: number[][]): number => {
    const ROWS = grid.length;
    const COLS = grid[0].length;
    const DIRS =  [[0, 1], [1, 0], [-1, 0], [0, -1]];

    const bfs = (row, col) => {
        const queue = new Queue<[number, number]>([[row, col]]);
        
        let area = 0;
        while (!queue.isEmpty()) {
            const [r, c] = queue.dequeue();

            if (r < 0 || c < 0 || r > ROWS - 1 || c > COLS - 1) continue;
            if (grid[r][c] === 0) continue;

            grid[r][c] = 0;
            area += 1;

            for (const [dx, dy] of DIRS) {
                queue.enqueue([r + dx, c + dy]);
            }
        }

        return area;
    };

    let maxArea = 0;
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (grid[r][c] === 1) {
                let area = bfs(r, c);
                maxArea = Math.max(maxArea, area);
            }
        }
    }

    return maxArea;
};