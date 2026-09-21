# 1295. Find Numbers with Even Number of Digits

**Difficulty:** Easy

## Problem Summary

Given a list of integers `nums`, return how many numbers contain an even number of digits.

For each number, determine how many digits it contains and check whether that count is even.

## Examples

```text
Input: nums = [12,345,2,6,7896]
Output: 2

Input: nums = [555,901,482,1771]
Output: 1
```

## Approach

Start with a counter `even_nums` set to `0` to keep track of how many numbers contain an even number of digits.

Iterate through each number in `nums`.

Convert the current integer to a string using `str()`, then use `len()` to determine how many digits it contains.

Use the modulo operator `%` to check whether the number of digits is even. If the digit count divided by `2` has a remainder of `0`, increment `even_nums`.

After checking every number, return `even_nums`.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

For this problem, each integer contains only a small bounded number of digits. More generally, if each number can contain up to `d` digits, converting each integer to a string gives a time complexity of O(n × d).

## Concepts Practiced

* Lists
* Iteration
* Counters
* Conditional statements
* Type conversion with `str()`
* Built-in functions (`len()`)
* Modulo operator (`%`)
* Checking even and odd values

## Notes

This problem demonstrates how converting data into a different representation can make a problem easier to solve.

Instead of using mathematical operations to count the digits of an integer, converting the number to a string allows `len()` to determine the digit count directly.

The expression:

`digit_number % 2 == 0`

checks whether the digit count is even. If the remainder after division by `2` is `0`, the number contains an even number of digits.

This problem also reinforces the common **counter pattern**: initialise a counter, iterate through the input, increment the counter whenever a condition is satisfied, and return the final count.
