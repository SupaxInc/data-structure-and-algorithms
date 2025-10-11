const topKFrequent = (nums: number[], k: number): number[] => {
    // + 1 since each index in array is a freq, so we need max number of freqs in an array
    const freqs = new Array(nums.length+1).fill(null).map(() => []);

    const count: Record<number, number> = {}; // (number, freq)
    for (let num of nums) count[num] = (count[num] || 0) + 1;

    for (let [key, val] of Object.entries(count)) freqs[val].push(Number(key));

    const result = [];
    for (let i = freqs.length-1; i >= 0; i--) {
        const freqsVal = freqs[i];

        for (let j = 0; j < freqsVal.length; j++) {
            if (result.length == k) return result;

            result.push(freqsVal[j]);
        }
    }

    return result;
};