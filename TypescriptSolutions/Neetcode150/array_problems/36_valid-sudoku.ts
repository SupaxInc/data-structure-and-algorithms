function isValidSudoku(board: string[][]): boolean {
    const rows: Record<number, Set<string>> = {};
    const cols: Record<number, Set<string>> = {};
    const squares: Record<string, Set<string>> = {};


    for (let r = 0; r < board.length; r++){
        for (let c = 0; c< board[r].length; c++) {
            const value = board[r][c];
            if (value == ".") continue;

            const squareKey: string = [Math.floor(r / 3), Math.floor(c/3)].toString();
            if (!rows[r]) rows[r] = new Set<string>();
            if (!cols[c]) cols[c] = new Set<string>();
            if (!squares[squareKey]) squares[squareKey] = new Set<string>();

            if (rows[r].has(value) || cols[c].has(value) || squares[squareKey].has(value)) {
                return false;
            }

            rows[r].add(value);
            cols[c].add(value);
            squares[squareKey].add(value);
        }
    }

    return true;
};