const lengthOfLongestSubstring = (s: string): number => {
    if (s.length  == 0) return 0;

    let start = 0;
    let longestSubstring = 0;
    const n = s.length;

    const subStringSet = new Set<string>();
    for (let end = 0; end < n; end++) {
        while (start < end && subStringSet.has(s[end])) {
            subStringSet.delete(s[start]);
            start++;
        }

        subStringSet.add(s[end]);
        longestSubstring = Math.max(end - start + 1, longestSubstring);
    }

    return longestSubstring;
};