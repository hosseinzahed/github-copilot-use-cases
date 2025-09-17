// The code below is a simple function that compares three numbers 
// and returns the sum of the positive ones.
function sumPositiveNumbers(a: number, b: number, c: number): number {
    if (a > 0) {
        if (b > 0) {
            if (c > 0) {
                return a + b + c;
            } else {
                return a + b;
            }
        } else {
            if (c > 0) {
                return a + c;
            } else {
                return a;
            }
        }
    } else {
        if (b > 0) {
            if (c > 0) {
                return b + c;
            } else {
                return b;
            }
        } else {
            if (c > 0) {
                return c;
            } else {
                return 0;
            }
        }
    }
}

// Prompt in Ask: Refactor the code to make it more readable and effective.