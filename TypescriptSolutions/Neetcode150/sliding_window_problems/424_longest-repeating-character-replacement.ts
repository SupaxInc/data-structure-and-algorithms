const notOptimizedCharacterReplacement = (s: string, k: number): number => {
    let start = 0;
    let longestString = 0;
    const n = s.length;
    
    const count: Record<string, number> = {};
    for (let end = 0; end < n; end++) {
        count[s[end]] = (count[s[end]] || 0) + 1;
        const highestCount = Math.max(...Object.values(count));

        while (start < end && ((end - start) + 1 - highestCount) > k) {
            count[s[start]]--;
            start++;
        }

        longestString = Math.max(longestString, (end - start) + 1);
    }

    return longestString;
}