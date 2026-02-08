export {};

const solve = (board: string[][]): void => {
    const ROWS = board.length;
    const COLS = board[0].length;
    const DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]];

    const borderRows = new Set<number>([0, ROWS - 1]);
    const borderCols = new Set<number>([0, COLS - 1]);

    const dfs = (row, col): void => {
        if (board[row][col] === "TEMP") return;

        board[row][col] = "TEMP";

        for (const [dx, dy] of DIRS) {
            const nr = row + dx;
            const nc = col + dy;

            if (nr < 0 || nc < 0 || nr > ROWS -1 || nc > COLS - 1) continue;

            if (board[nr][nc] === "X") continue;

            dfs(nr, nc)
         }    

         return;
    };

    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            if ((borderRows.has(row) || borderCols.has(col)) && board[row][col] === "O") {
                dfs(row, col);
            }
        }
    }

    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            if (board[row][col] === "O") board[row][col] = "X";
        }
    }

    for (let row = 0; row < ROWS; row++) {
        for (let col = 0; col < COLS; col++) {
            if (board[row][col] === "TEMP") board[row][col] = "O";
        }
    }
};