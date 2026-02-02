export {};
const findOrder = (numCourses: number, prerequisites: number[][]): number[] => {
    const preMap: Record<number, number[]> = {};

    for (let i = 0; i < numCourses; i++) preMap[i] = [];

    // Courses -> Prerequisites
    for (const [crs, pre] of prerequisites) {
        preMap[crs].push(pre);
    }

    const visit = new Set<number>();
    const completed = new Set<number>();

    const dfs = (crs: number): boolean => {
        if (visit.has(crs)) return false;
        if (completed.has(crs)) return true;

        visit.add(crs);

        for (const pre of preMap[crs]) {
            if (!dfs(pre)) return false;
        }

        completed.add(crs);
        visit.delete(crs);

        return true;
    };

    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) return [];
    }

    return [...completed];
};