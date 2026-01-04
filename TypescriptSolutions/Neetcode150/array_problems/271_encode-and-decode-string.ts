class Solution {
    public decoder:  string;

    constructor() {
        this.decoder = "#";
    }

    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs): string {
        return strs.map(str => `${str.length}${this.decoder}${str}`).join('');
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str): string[] {
        const decoded: string[] = [];
        let i = 0;

        while (i < str.length) {
            const j = str.indexOf(this.decoder, i);
            const n = parseInt(str.slice(i, j+1));

            const decodedStr = str.slice(j+1, j+n+1);
            decoded.push(decodedStr);

            i = j + n + 1;
        }

        return decoded;
    }
}
