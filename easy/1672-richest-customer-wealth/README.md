# 1672. Richest Customer Wealth

**Difficulty:** Easy

## Problem Summary

Given a 2D list `accounts`, where each inner list represents the amount of money a customer has across multiple bank accounts, return the wealth of the richest customer.

A customer's total wealth is the sum of all values in their list of accounts.

## Examples

```text
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
```

## Approach

Start with a variable `richest_person` set to `0` to keep track of the greatest wealth found so far.

Iterate through each customer's accounts and use `sum()` to calculate that customer's total wealth.

Then use `max()` to compare the current customer's wealth with the greatest wealth found so far. Store whichever value is larger back in `richest_person`.

After every customer has been checked, return `richest_person`.

## Complexity

* **Time:** O(m × n)
* **Space:** O(1)

Where `m` is the number of customers and `n` is the number of bank accounts per customer.

## Concepts Practiced

* Lists
* 2D lists
* Iteration
* Accumulating values
* Built-in functions (`sum()` and `max()`)
* Tracking the maximum value
* Updating state during iteration

## Notes

This problem introduces the useful pattern of keeping track of the **best value seen so far**.

For each customer, their total wealth is calculated once using `sum()`. That value is then compared with the current maximum:

`richest_person = max(richest_person, account_total)`

This avoids needing to store every customer's total wealth before determining the maximum.

The same pattern appears frequently in algorithm problems when tracking values such as the largest number, smallest number, highest score, maximum profit, or longest sequence.
