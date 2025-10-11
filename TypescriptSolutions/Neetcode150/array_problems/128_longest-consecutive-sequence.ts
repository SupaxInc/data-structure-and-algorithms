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