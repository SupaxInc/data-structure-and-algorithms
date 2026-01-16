const search = (nums: number[], target: number): number => {
    let lo = 0;
    let hi = nums.length - 1;

    while (lo <= hi) {
        const mid = lo + Math.floor((hi - lo) / 2);

        if (nums[mid] === target) {
            return mid;
        }

        if (nums[mid] > nums[hi]) {
            if (target < nums[lo] || target > nums[mid]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        } else {
            if (target > nums[hi] || target < nums[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
    }

    return - 1;
};