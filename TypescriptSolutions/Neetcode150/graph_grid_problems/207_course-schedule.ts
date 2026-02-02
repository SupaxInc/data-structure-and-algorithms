export {};
const canFinish = (numCourses: number, prerequisites: number[][]): boolean => {
    const preMap: Record<number, number[]> = {};

    for (let i = 0; i < numCourses; i++) preMap[i] = [];

    // Course -> Prereq
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

    for (let crs = 0; crs < numCourses; crs++) {
        if (!dfs(crs)) return false;
    }

    return true;
};