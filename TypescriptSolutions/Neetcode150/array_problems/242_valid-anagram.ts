function isSolution1Anagram(s: string, t: string): boolean {
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

const isSolution2Anagram = (s: string, t:string): boolean => {
    if (s.length != t.length) return false;

    const count: Record<string, number> = {};

    for (let i = 0; i < s.length; i++) count[s[i]] = (count[s[i]] || 0) + 1;

    for (let i = 0; i < t.length; i++) {
        // Handles counts that go to 0 and if the character exists
        if (!count[t[i]]) return false;

        count[t[i]]--;
    }

    return true;
}