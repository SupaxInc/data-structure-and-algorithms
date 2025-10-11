class Solution {
    encode(strs: string[]): string {
        return strs.map((str) => `${str.length}#${str}`).join('');
    }

    decode(str: string): string[] {
        const n = str.length;
        let idx = 0;
        const res: string[] = []

        while (idx < n) {
            let j = idx;

            while (str[j] != "#") j++;

            const len = parseInt(str.slice(idx, j));
            const start = j + 1;
            res.push(str.slice(start, len + start));

            idx = len + start;
        }

        return res;
    }
}