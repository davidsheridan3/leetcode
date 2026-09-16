# 1480. Running Sum of 1d Array

**Difficulty:** Easy

## Problem Summary

Given a list of integers `nums`, return a new list containing the running sum of the input list.

The running sum at each position is the sum of the current number and all numbers that came before it.

## Examples

```text
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

## Approach

Create an empty result list and a variable called `running_total` starting at `0`.

Iterate through each number in `nums`. Add the current number to `running_total`, then append the updated total to the result list.

By keeping track of the running total, there is no need to recalculate the sum of all previous elements during each iteration.

Finally, return the completed result list.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

## Concepts Practiced

* Lists
* Iteration
* Variables
* Accumulating values
* `append()`
* State tracking
* Prefix sums

## Notes

This problem introduces the idea of maintaining a value as you iterate through a list. Instead of repeatedly calculating the sum from the beginning of the array, a `running_total` stores the sum calculated so far.

This is an early example of the **prefix sum** pattern, where information about previous elements is accumulated and reused instead of being recalculated. The same idea appears in more advanced problems involving subarray sums and range queries.
