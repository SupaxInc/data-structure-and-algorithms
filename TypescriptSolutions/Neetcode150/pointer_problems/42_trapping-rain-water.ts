const trap = (height: number[]): number => {
    const n = height.length;
    const maxLefts: number[] = [];
    const maxRights: number[] = new Array(n).fill(0);

    let maxLeft = 0;
    for (let i=0; i<n; i++) {
        maxLefts.push(maxLeft);
        maxLeft = Math.max(maxLeft, height[i]);
    }

    // becareful here, ts doesn't accept negative indices like python
    // e.g. maxRight = maxRights[-1]
    let maxRight = 0;
    for (let i= n-1; i>=0; i--) {
        maxRights[i] = maxRight;
        maxRight = Math.max(maxRight, height[i]);
    }

    let total = 0;
    for (let i=0; i<n; i++) {
        const units = Math.min(maxLefts[i], maxRights[i]) - height[i];
        
        // filters out negative units
        if (units > 0) {
            total += units;
        }
    }

    return total;
};