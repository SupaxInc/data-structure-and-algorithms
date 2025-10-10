function containsDuplicate(nums: number[]): boolean {
    const numsSet = new Set<number>();

    for (let i = 0; i < nums.length; i++) {
        if (numsSet.has(nums[i])) {
            return true;
        }

        numsSet.add(nums[i]);
    }

    return false;
};