const checkInclusion = (s1: string, s2: string): boolean => {
    if (s1.length > s2.length) return false;

    const s1Count = new Map<string, number>();
    for (const char of s1) {
        s1Count.set(char, (s1Count.get(char) ?? 0) + 1);
    }

    let start = 0;
    let matches = 0;
    for (let end = 0; end < s2.length; end++) {
        if (s1Count.has(s2[end])) {
            s1Count.set(s2[end], s1Count.get(s2[end])! - 1);
            if (s1Count.get(s2[end]) == 0) matches++;
        }

        if ((end - start) + 1 > s1.length) {
            if (s1Count.has(s2[start])) {
                if(s1Count.get(s2[start]) == 0) matches--;
                s1Count.set(s2[start], s1Count.get(s2[start])! + 1);
            }

            start++;
        }

        // Use distinct letters from the count frequency
        if (matches == s1Count.size) return true;
    }

    return false;
};