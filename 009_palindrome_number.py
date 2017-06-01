class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            string = str(x)
            if string == string[::-1]:
                return True
            else:
                return False