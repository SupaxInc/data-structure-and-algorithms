const checkInclusion = (s1: string, s2: string): boolean => {
    const k = s1.length;
    if (s2.length < k) {
        return false;
    }

    const s1Count: Record<string, number> = {};
    for (const c of s1) {
        s1Count[c] = (s1Count[c] ?? 0) + 1;
    }

    let start = 0;
    let matchLength = 0;
    const required = Object.keys(s1Count).length;

    for (let end = 0; end < s2.length; end++) {
        if (s2[end] in s1Count) {
            s1Count[s2[end]]--;
            if (s1Count[s2[end]] === 0) matchLength++;
        }

        if (end > k - 1) {
            if (s2[start] in s1Count) {
                if (s1Count[s2[start]] === 0) matchLength--;
                s1Count[s2[start]]++;
            }
            start++;
        }

        if (matchLength === required) {
            return true;
        }
    }

    return false;
};