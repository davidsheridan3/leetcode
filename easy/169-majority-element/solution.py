class Solution(object):
    def majorityElement(self, nums):
        counts = {} # holds number counts
        majority_threshold = len(nums) // 2 # defines majority value
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            if counts[num] > majority_threshold:
                return num