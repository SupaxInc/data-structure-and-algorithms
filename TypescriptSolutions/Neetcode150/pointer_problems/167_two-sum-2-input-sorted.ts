const twoSum = (numbers: number[], target: number): number[] => {
    let l = 0;
    let r = numbers.length - 1;

    while (l < r) {
        const total = numbers[l] + numbers[r];

        if (total === target) {
            return [l + 1, r + 1];
        }

        if (total < target) {
            l += 1;
        } else {
            r -= 1;
        }
    }

    return [];
};