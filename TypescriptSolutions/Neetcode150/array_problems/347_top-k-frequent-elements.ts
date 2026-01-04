const topKFrequent = (nums: number[], k: number): number[] => {
    const n = nums.length + 1;
    const res: number[] = [];

    const count: Record<number, number> = {};
    for (const num of nums) {
        if (!count[num]) count[num] = 0;
        count[num] += 1;
    }

    const elemArr: number[][] = new Array(n).fill(null).map(val => []);
    for (const [key, val] of Object.entries(count)) {
        elemArr[val].push(Number(key));
    }

    for (let i = n-1; i >= 0; i--) {
        const item = elemArr[i];
        for (const num of item) {
            if (res.length === k) return res;
            res.push(num);
        }
    }

    return res;
};