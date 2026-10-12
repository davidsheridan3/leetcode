# 169. Majority Element

**Difficulty:** Easy

## Problem Summary

Given a list of integers `nums`, return the majority element.

The majority element is the value that appears more than half of the total number of elements in the list.

The problem guarantees that a majority element always exists.

## Examples

```text
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Approach

Create an empty dictionary called `counts` to keep track of how many times each number appears.

Calculate the majority threshold using `len(nums) // 2`.

Iterate through each number in `nums`. If the number already exists in `counts`, increase its count by `1`. Otherwise, add it to the dictionary with an initial count of `1`.

After updating the current number's count, check whether its count has exceeded the majority threshold. If it has, return that number immediately.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

## Concepts Practiced

* Lists
* Dictionaries
* Key-value pairs
* Iteration
* Conditional statements
* Frequency counting
* Dictionary membership using `in`
* Updating dictionary values
* Integer division (`//`)
* Early returns
* Python indentation and control flow

## Notes

This problem introduces the common **frequency counting** pattern using a dictionary.

Each number is stored as a dictionary key, while its value represents how many times that number has been encountered.

For example:

```text
nums = [2,2,1,2]

counts = {
    2: 3,
    1: 1
}
```

The majority threshold is calculated using:

`len(nums) // 2`

As soon as a number's count becomes greater than this threshold, it can be returned because the problem guarantees that a majority element exists.

The placement of the majority check inside the `for` loop is important. It allows each number to be checked immediately after its frequency is updated rather than only checking the final number after iteration has finished.

This solution runs in **O(n) time** but requires **O(n) additional space** for the dictionary.

The optional follow-up can be solved in O(1) extra space using the **Boyer-Moore Voting Algorithm**, but the dictionary approach provides a clear introduction to frequency counting and hash maps.