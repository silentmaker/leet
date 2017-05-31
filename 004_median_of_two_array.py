class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        return self.findListMedian(nums3)

    def findListMedian(self, nums):
        length = len(nums)

        if length == 1:
            return nums[0]
        elif length == 2:
            return float((nums[0] + nums[1])) / 2
        elif length % 2 == 0:
            return float((nums[length / 2 - 1] + nums[length / 2])) / 2
        else:
            return nums[length / 2]