const productExceptSelf = (nums: number[]): number[] => {
    const n = nums.length;
    if (n < 2) {
        return [];
    }

    const res: number[] = [];

    const prefix = [nums[0]]
    for (let i = 1; i < n; i++) {
        prefix.push(nums[i] * prefix[i-1]);
    }

    const postfix = new Array(n).fill(1);
    postfix[n - 1] = nums[n - 1];
    for (let i = n - 2; i > 0; i--) {
        postfix[i] = nums[i] * postfix[i+1];
    }

    for (let i = 0; i < n; i++) {
        if (i === 0) {
            res.push(1 * postfix[i + 1]);
        } else if (i === n - 1) {
            res.push(1 * prefix[i - 1]);
        } else {
            res.push(prefix[i - 1] * postfix[i + 1]);
        }
    }

    return res;
};

const productExceptSelfBetterSpaceSolution = (nums: number[]): number[] => {
    const n = nums.length;
    if (n < 2) {
        return [];
    }

    const res = new Array(n).fill(1);

    let prefixProduct = 1;
    for (let i = 0; i < n; i++) {
        res[i] = prefixProduct;
        prefixProduct *= nums[i];
    };

    let postfixProduct = 1;
    for (let i = n - 1; i >= 0; i--) {
        res[i] *= postfixProduct;
        postfixProduct *= nums[i];
    }

    return res;
};