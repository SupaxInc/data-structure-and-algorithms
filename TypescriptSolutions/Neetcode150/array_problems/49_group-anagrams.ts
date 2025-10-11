const groupAnagrams = (strs: string[]): string[][] => {
    if (strs.length < 2) return [strs];
    
    const groups: Record<string, string[]> = {};

    for (let str of strs) {
        const freqs = new Array(26).fill(0);
        const baseCharNum = "a".charCodeAt(0); // 97

        for (let char of str) freqs[char.charCodeAt(0) - baseCharNum]++;

        const freqString = freqs.toString();
        if (!groups[freqString]) groups[freqString] = [];
        groups[freqString].push(str);
    }

    return Object.values(groups);
};