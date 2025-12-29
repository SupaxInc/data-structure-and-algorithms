const isValidReadadbleSolution = (s: string): boolean => {
    const complement: Record<string, string> = {
        ']' : '[',
        ')' : '(',
        '}' : '{',
    };

    const stack: string[] = [];

    for (const char of s) {
        // If it is a closing bracket
        if (complement[char] !== undefined) {
            // Check 1: Stack is not empty, therefore cannot be matched
            // Check 2: Unable to match complementary brackcet
            if (stack.length === 0 || stack.pop() !== complement[char]) {
                return false;
            }
        } else {
            stack.push(char);
        }
    }

    // Ensure stack is empty
    return stack.length === 0;
};

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