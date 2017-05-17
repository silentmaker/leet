class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0
        j = 1
        length = len(nums)
        
        while i <= length - 2:
            if nums[i] + nums [j] == target:
                return [i, j]
                break
            else:
                j = j + 1
                if j == length:
                    i = i + 1
                    j = i + 1