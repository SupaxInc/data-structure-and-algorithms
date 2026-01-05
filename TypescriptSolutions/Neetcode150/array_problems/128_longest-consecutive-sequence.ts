function longestConsecutive(nums: number[]): number {
    const numSet = new Set(nums);
    let maxLength = 0;

    for (const num of numSet) {
        let length = 0;
        // Check if there are any left neighbors so you ONLY start at beginning of a sequence
        if (!numSet.has(num-1)) {
            // Begin sequence!
            
            // Check if the sequence contains CONSECUTIVE new numbers
            // Use length to find consecutive sequence
            while (numSet.has(num + length)) length++;

            // Find if it has a higher max than other sequences
            maxLength = Math.max(maxLength, length);
        }
    }

    return maxLength;
};

const alternative = (nums: number[]): number => {
    let longest = 0;
    const numSet = new Set<number>(nums);

    for (const num of numSet) {
        if (!numSet.has(num - 1)) {
            let length = 0;
            let sequenceNum = num;

            while (numSet.has(sequenceNum)) {
                length += 1;
                sequenceNum += 1;
            }

            longest = Math.max(longest, length);
        }
    }

    return longest;
 };