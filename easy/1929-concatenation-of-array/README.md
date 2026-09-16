# 1929. Concatenation of Array

**Difficulty:** Easy

## Problem Summary

Given a list of integers `nums`, create and return a new list containing `nums` twice in the same order.

If `nums` has a length of `n`, the resulting list will have a length of `2n`.

## Examples

```text
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
```

## Approach

Create the result by concatenating the `nums` list with itself.

In Python, the `+` operator can be used with lists to combine them into a new list. Therefore, `nums + nums` produces a list containing all elements of `nums` followed by the same elements again.

Return the newly created list.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

## Concepts Practiced

* Lists
* List concatenation
* The `+` operator with lists
* Returning values
* Python sequence operations

## Notes

This problem reinforces how Python's operators can behave differently depending on the type of object being used. With integers, `+` performs arithmetic addition, while with lists it performs concatenation.

Although the solution can be written very concisely, creating the concatenated list still requires copying the elements into a new list. Therefore, the operation takes O(n) time and requires O(n) additional space.

This is a useful reminder that short Python code does not necessarily mean constant-time work is being performed behind the scenes.
