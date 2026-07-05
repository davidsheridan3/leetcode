# 1431. Kids With the Greatest Number of Candies

**Difficulty:** Easy

## Problem Summary

Given a list of integers representing the number of candies each child has and an integer representing the number of extra candies available, determine whether each child could have the greatest number of candies if they received all of the extra candies.

Return a list of boolean values where each element indicates whether the corresponding child can have the greatest number of candies.

## Examples

```text
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [True, True, True, False, True]

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [True, False, False, False, False]

Input: candies = [12,1,12], extraCandies = 10
Output: [True, False, True]
```

## Approach

First, find the current maximum number of candies any child has using `max()`. Then, iterate through the list and check whether each child would have at least that many candies after receiving the extra candies. Append `True` or `False` to the result list based on the comparison.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

## Concepts Practiced

* Lists
* Iteration
* Conditional statements
* Built-in functions (`max()`)
* Boolean values

## Notes

This problem introduces the idea of solving a problem efficiently by computing a useful value once—in this case, the current maximum number of candies—instead of repeatedly comparing every child against every other child. It also reinforces building and returning a list of boolean values.
