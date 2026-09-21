class Solution(object):
    def findNumbers(self, nums):
        even_nums = 0
        for num in nums:
            digit_number = len(str(num))
            if digit_number % 2 == 0:
                even_nums += 1
        return even_nums