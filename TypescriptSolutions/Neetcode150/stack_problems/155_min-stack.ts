class MinStack {
    private stack: [number, number][] = []; // (val, min)

    push(val: number): void {
        const n = this.stack.length;
        const min = n > 0 ? Math.min(val, this.stack[n-1][1]) : val;

        this.stack.push([val, min]);
    }

    pop(): void {
        this.stack.pop();
    }

    top(): number {
        return this.stack[this.stack.length-1][0]
    }

    getMin(): number {
        return this.stack[this.stack.length-1][1]
    }
}

class SimplerMinStack {
    // Uses a "tuple" (val, minimum val)
    constructor(private stack: number[][] = []) {}

    push(val: number): void {
        if (this.stack.length > 0) {
            this.stack.push([val, Math.min(val, this.getMin())]);
        } else {
            this.stack.push([val, val]);
        }
    }

    pop(): void {
        this.stack.pop();
    }

    top(): number {
        return this.stack[this.stack.length-1][0];
    }

    getMin(): number {
        return this.stack[this.stack.length-1][1];
    }
}