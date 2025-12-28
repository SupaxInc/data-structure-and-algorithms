const containsDuplicate = (nums: number[]): boolean => {
    const mySet = new Set<number>();

    for(const num of nums) {
        if (mySet.has(num)) return true;

        mySet.add(num);
    }

    return false;
};