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

const twoSum2 = (nums: number[], target: number): number[] => {
    const counts: Record<number, number> = {};

    for (let i = 0; i < nums.length; i++) {
        const complementary = target - nums[i];

        if (counts[complementary] !== undefined) {
            return [counts[complementary], i];
        }

        counts[nums[i]] = i;
    }

    return [];
}