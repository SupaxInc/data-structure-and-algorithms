function isAnagram(s: string, t: string): boolean {
    type CharCount = Record<string, number>;

    if (s.length != t.length) return false;

    const countAnagram = (anagramString: string): CharCount => {
        const countMap: CharCount = {};

        for(const char of anagramString) {
            countMap[char] = (countMap[char] || 0) + 1;
        }

        return countMap;
    };

    const a = countAnagram(s);
    const b = countAnagram(t);

    for (let char of s) {
        if (!(char in b)) {
            return false;
        }
        if (a[char] != b[char]) {
            return false;
        }
    }

    return true;
};