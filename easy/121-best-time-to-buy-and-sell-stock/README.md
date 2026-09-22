# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy

## Problem Summary

Given a list `prices`, where each value represents the price of a stock on a particular day, return the maximum profit that can be made by buying the stock on one day and selling it on a later day.

The stock must be bought before it is sold.

If no profitable transaction is possible, return `0`.

## Examples

```text
Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0
```

## Approach

Keep track of two values while iterating through the prices: the lowest price seen so far and the maximum profit found so far.

Start `min_price` with the first price in the list and `max_profit` at `0`.

For each price, update `min_price` if the current price is lower than the cheapest price seen so far.

Then calculate the profit that would be made if the stock were sold at the current price after buying at `min_price`.

If this profit is greater than `max_profit`, update the maximum profit.

After checking every price, return `max_profit`.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Concepts Practiced

* Lists
* Iteration
* Conditional statements
* State tracking
* Tracking a minimum value
* Tracking a maximum value
* Greedy problem solving
* Calculating values during iteration

## Notes

This problem reinforces the idea of maintaining useful information while iterating through a list.

Instead of finding the overall minimum and maximum prices, the algorithm keeps track of the **lowest price seen so far**. This is important because the stock must be bought before it can be sold.

For every price, the potential profit is calculated using:

`profit = price - min_price`

The best profit found so far is then stored in `max_profit`.

This introduces an important problem-solving pattern: **use information from the past to determine the best decision available at the current position**.

It also demonstrates why finding the global minimum and global maximum independently is not always sufficient when the ordering of values matters.
