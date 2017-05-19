class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        med1 = self.findListMedian(nums1)
        med2 = self.findListMedian(nums2)

        while med1 != med2:
            if med1 < med2:
                nums1 = self.rightList(nums1, len1)
                nums2 = self.leftList(nums2, len2)
            else:
                nums1 = self.leftList(nums1, len1)
                nums2 = self.rightList(nums2, len2)
            
            len1 = len(nums1)
            len2 = len(nums2)
            med1 = self.findListMedian(nums1)
            med2 = self.findListMedian(nums2)
                    
            if len1 <= 2 and len2 <= 2:
                break
            
        if med1 == med2:
            return med1
        elif len1 + len2 == 4:
            return self.findListMedian([med1, med2])
        elif len1 + len2 == 3:
            nums3 = nums1 + nums2
            nums3.sort()
            return nums3[1]
        elif len1 + len2 == 2:
            return self.findListMedian([nums1[0], nums2[0]])

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

    def leftList(self, nums, length):
        if length > 2 and length % 2 == 0:
            nums = nums[:length / 2]
        elif length > 2 and length % 2 == 1:
            nums = nums[:length / 2 + 1]
        return nums

    def rightList(self, nums, length):
        if length > 2 and length % 2 == 0:
            nums = nums[length / 2:]
        elif length > 2 and length % 2 == 1:
            nums = nums[length / 2:]
        return nums