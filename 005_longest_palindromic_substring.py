class Solution(object):
    def longestPalindrome(self, s):
        # palindromic means reversing the string gets the same string, eg: dad, abcba, ...
        # assume that the palindromic string have a length less than 1000

        palindromic_str = ''
        step = 0
        i = 1
        
        if s == s[::-1]:
            return s

        while i < len(s):
            while i - step >= 0 and i + step < len(s) and s[i - step] == s[i + step]:
                if 2 * step + 1 >= len(palindromic_str):
                    palindromic_str = s[i - step:i + step + 1]
                step = step + 1
            step = 0
            
            if s[i] == s[i - 1]:
                while i - step - 1 >= 0 and i + step < len(s) and s[i - step - 1] == s[i + step]:
                    if 2 * step + 2 >= len(palindromic_str):
                        palindromic_str = s[i - step - 1:i + step + 1]
                    step = step + 1
                step = 0

            i = i + 1

        return palindromic_str