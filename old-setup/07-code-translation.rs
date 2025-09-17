// The following rust function calculates the sum of all even numbers in a given vector.
fn sum_of_evens(numbers: Vec<i32>) -> i32 {
    let mut sum = 0;
    for &number in &numbers {
        if number % 2 == 0 {
            sum += number;
        }
    }
    sum
}

// Prompt: Translate the code into python, typescript, and C#