const threeSum = (nums: number[]): number[][] => {
    const res: number[][] = []
    const n = nums.length;
    nums.sort((a, b) => a - b)

    for (let i = 0; i < n - 2; i++) {
        if ((i > 0) && nums[i] === nums[i-1]) {
            continue;
        }

        let l = i + 1;
        let r = n - 1;
        while (l < r) {
            const total = nums[i] + nums[l] + nums[r];

            if (total < 0) {
                l += 1;
            } else if (total > 0) {
                r -= 1
            } else {
                res.push([nums[i], nums[l], nums[r]]);

                l += 1
                while ((l < r) && (nums[l] === nums[l-1])) l +=1;
            }
        }

    }

    return res;
};