const minWindow = (s: string, t: string): string => {
    let res: [number, number] = [0, 0]; // tuple
    let resLen = Infinity; // in the event we don't find a substring

    const tCount = new Map<string, number>();
    const sCount = new Map<string, number>();
    for (let char of t) tCount.set(char, (tCount.get(char) ?? 0) + 1);

    const need = tCount.size; // The size of the frequency dictionary not string size
    let start = 0, have = 0;
    for (let end = 0; end < s.length; end++) {
        sCount.set(s[end], (sCount.get(s[end]) ?? 0) + 1 );
        // Check if both counts are the same, if it is then it matched the amount of character for the specific character
        if (sCount.get(s[end]) === tCount.get(s[end])) {
            have++;
        }

        while (have === need) {
            // Check if current window length is less than the current result substring length
            if ((end - start + 1) < resLen) {
                resLen = end - start + 1;
                res = [start, end + 1];
            }

            sCount.set(s[start], (sCount.get(s[start]) ?? 0) - 1);
            if ((sCount.get(s[start]) ?? 0) < (tCount.get(s[start]) ?? 0)) {
                have--;
            }

            start++;
        }
    }

    return resLen !== Infinity ? s.slice(res[0], res[1]) : "";
};