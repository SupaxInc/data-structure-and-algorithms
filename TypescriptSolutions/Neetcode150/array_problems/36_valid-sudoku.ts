const isValidSudoku = (board: string[][]): boolean =>  {
    const rows: Record<string, Set<string>> = {};
    const cols: Record<string, Set<string>> = {};
    const squares: Record<string, Set<string>> = {};

    const ROWS = board.length;
    const COLS = board[0].length;

    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            const val = board[r][c];
            if (val === ".") continue;

            const squareKey = [Math.floor(r / 3), Math.floor(c / 3)].toString();
            if (!rows[r]) rows[r] = new Set<string>();
            if (!cols[c]) cols[c] = new Set<string>();
            if (!squares[squareKey]) squares[squareKey] = new Set<string>();

            if (rows[r].has(val) || cols[c].has(val) || squares[squareKey].has(val)) {
                return false;
            }

            rows[r].add(val);
            cols[c].add(val);
            squares[squareKey].add(val);
        }
    }

    return true;
}