class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        buff = {}
        max = 0
        count = 0
        i = 0
        length = len(s)
        
        while i < length:
            if s[i] in buff:
                i = buff[s[i]]
                if count > max:
                	max = count
                buff = {}
            	count = 0
            else:
                buff[s[i]] = i
                count = count + 1
            i = i + 1
        if count > max:
            max = count
        return max