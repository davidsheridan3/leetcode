class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current_ones = 0
        max_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0

        return max_ones