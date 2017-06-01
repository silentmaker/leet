class Solution(object):
    def convert(self, s, numRows):
        result = ''
        swing = 2 * numRows - 2

        if numRows < 2:
            return s

        for i in range(numRows):
            pos = i
            step = swing - 2 * i
            if i + 1 == numRows:
                step = swing
            while pos < len(s):
                result = result + s[pos]
                pos = pos + step
                if step != swing:
                    step = swing - step
        return result