const isValid = (s: string): boolean => {
    let stack: string[] = [];
    let mapping: Record<string, string> = {
        ']' : '[',
        ')' : '(',
        '}' : '{'
    };

    for (let char of s) {
        // If it is an open bracket add to stack
        if (!(char in mapping)) {
            stack.push(char);
        } else {
            // Fail if top of stack (LIFO) does not equal CURRENT parentheses character
            if (stack.pop() !== mapping[char]) {
                return false;
            }
        }
    }

    // We may just be pushing to stack without ever finding a closing parentheses
    return stack.length === 0;
};