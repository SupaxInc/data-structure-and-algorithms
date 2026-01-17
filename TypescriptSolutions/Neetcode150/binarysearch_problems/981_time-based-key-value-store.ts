type TimeMapValues = [string, number][]; // A list of [value, timestamp]

class TimeMap {
    private timeMap: Map<string, TimeMapValues> = new Map<string, TimeMapValues>();

    set(key: string, value: string, timestamp: number): void {
        let values = this.timeMap.get(key);
    
        if (!values) {
            values = [];
            this.timeMap.set(key, values);
        }
    
        values.push([value, timestamp]);
    }

    get(key: string, timestamp: number): string {
        const values = this.timeMap.get(key);
        if (!values) {
            return "";
        }

        let lo = 0;
        let hi = values.length - 1;
        let currValue = "";

        while (lo <= hi) {
            const mid = lo + Math.floor((hi - lo) / 2);
            const midValue = values[mid][0];
            const midTimestamp = values[mid][1];

            if (midTimestamp <= timestamp) {
                currValue = midValue;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return currValue;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */