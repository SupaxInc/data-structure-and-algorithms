export {};
import { Queue } from "@datastructures-js/queue";

const orangesRotting = (grid: number[][]): number => {
    const ROWS = grid.length;
    const COLS = grid[0].length;
    const DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]];

    let fresh = 0
    const queue = new Queue<[number, number]>();
    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            if (grid[row][col] === 2) {
                queue.enqueue([row, col]);
            } else if (grid[row][col] === 1) {
                fresh++;
            }
        }
    }

    if (fresh === 0) return 0;

    let minutes = 0;
    while (!queue.isEmpty()) {
        const levelSize = queue.size();
        for (let i = 0; i < levelSize; i++) {
            const [row, col] = queue.dequeue()!;

            for (const [dx, dy] of DIRS) {
                const nr = row + dx;
                const nc = col + dy;

                if (nr < 0 || nc < 0 || nr > ROWS - 1 || nc > COLS - 1) continue;
                if (grid[nr][nc] === 0 || grid[nr][nc] === 2) continue;

                grid[nr][nc] = 2;
                fresh--;
                queue.enqueue([nr, nc]);
            }
        }

        if (queue.size() > 0) minutes++;
    }

    return fresh > 0 ? -1 : minutes;
};