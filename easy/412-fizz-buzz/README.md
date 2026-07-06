412. Fizz Buzz

Difficulty: Easy

Problem Summary

Given an integer n, return a list of strings representing the numbers from 1 to n.

For each number:

Return "FizzBuzz" if it is divisible by both 3 and 5.
Return "Fizz" if it is divisible by 3.
Return "Buzz" if it is divisible by 5.
Otherwise, return the number as a string.
Examples
Input: n = 3
Output: ["1", "2", "Fizz"]

Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]

Input: n = 15
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
Approach

Iterate through the numbers from 1 to n. For each number, use the modulo (%) operator to determine divisibility.

Check if the number is divisible by both 3 and 5 first, followed by checking divisibility by 3 and 5 individually. Append the appropriate string to the result list, or the number converted to a string if none of the conditions are met.

Complexity
Time: O(n)
Space: O(n)
Concepts Practiced
Loops
Conditional statements
Modulo operator (%)
Lists
String conversion
Order of condition evaluation
Notes

Fizz Buzz is a classic programming exercise used to practice loops, conditional logic, and the modulo operator. It also highlights the importance of checking the most specific condition (FizzBuzz) before the individual cases (Fizz and Buzz).