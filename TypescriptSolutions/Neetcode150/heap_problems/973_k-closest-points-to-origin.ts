export {};

import {
    MinHeap,
  } from '@datastructures-js/heap';

const kClosest = (points: number[][], k: number): number[][] => {
    const res: number[][] = [];

    // store [dist, x, y] like Python
    // in datastructures lib, you need to specify what index in the array will be used as comparator root
    const minHeap = new MinHeap((v: number[]) => v[0]);

    for (const [x, y] of points) {
    minHeap.insert([x**2 + y**2, x, y]);
    }

    for (let i = 0; i < k; i++) {
    const item = minHeap.extractRoot();
    if (!item) break;
    const [_, x, y] = item;
    res.push([x, y]);
    }

    return res;
};