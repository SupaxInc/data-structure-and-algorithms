const findMin = (nums: number[]): number => {
    let lo = 0;
    let hi = nums.length - 1;
    let minNum = Infinity;

    while (lo <= hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        minNum = Math.min(minNum, nums[mid]);

        if (nums[mid] > nums[hi]) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    return minNum;
};