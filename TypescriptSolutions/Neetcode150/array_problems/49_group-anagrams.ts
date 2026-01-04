const groupAnagrams = (strs: string[]): string[][] => {
    const groups: Record<string, string[]> = {};

    for (const str of strs) {
        const counts = new Array(26).fill(0);

        for (const c of str) {
            const idx = c.charCodeAt(0) - 'a'.charCodeAt(0);
            counts[idx]++;
        }
        
        // Can use .toString() here as well
        const countStr = counts.join(',');

        // Records will be undefined at first and need to set an array
        if (!groups[countStr]) groups[countStr] = [];
        groups[countStr].push(str);
    }

    // Object.values cocnverts to array -> groups values are also already array so creates 2d array
    return Object.values(groups);
};