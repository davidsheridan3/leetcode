# 485. Max Consecutive Ones

**Difficulty:** Easy

## Problem Summary

Given a binary list `nums` containing only `0`s and `1`s, return the maximum number of consecutive `1`s found in the list.

A sequence of `1`s is consecutive when there are no `0`s between them.

## Examples

```text
Input: nums = [1,1,0,1,1,1]
Output: 3

Input: nums = [1,0,1,1,0,1]
Output: 2
```

## Approach

Use two variables to track the current streak of consecutive `1`s and the longest streak found so far.

Iterate through each number in `nums`.

If the current number is `1`, increase `current_ones` by one. Then compare the current streak with `max_ones` using `max()` and keep whichever value is larger.

If the current number is `0`, reset `current_ones` to `0` because the consecutive sequence has been broken.

After checking every number, return `max_ones`.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Concepts Practiced

* Lists
* Iteration
* Conditional statements
* Counters
* State tracking
* Resetting state
* Built-in functions (`max()`)
* Tracking the maximum value

## Notes

This problem reinforces the difference between **current state** and **best state seen so far**.

`current_ones` represents the length of the consecutive sequence currently being examined. When a `0` is encountered, this value must be reset because the streak has ended.

`max_ones` stores the longest streak encountered at any point and is not reset when a `0` is found.

The pattern:

`max_ones = max(max_ones, current_ones)`

is another example of maintaining the best value seen so far. Unlike the previous Richest Customer Wealth problem, this problem also introduces the idea of **resetting temporary state when a condition breaks a sequence**.

This combination of tracking a current value and a historical maximum appears frequently in problems involving streaks, sequences, subarrays, and strings.
