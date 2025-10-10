function twoSum(nums: number[], target: number): number[] {
    const targetCache = new Map<number, number>();

    for (let i=0; i < nums.length; i++) {
        const numNeeded = target - nums[i];
        if (targetCache.has(numNeeded)) {
            return [targetCache.get(numNeeded)!, i];
        }

        targetCache.set(nums[i], i)
    }

    return [];
};