class Solution(object):
    def reverse(self, x):
        # The input is assumed to be a 32-bit signed integer. 
        # Function should return 0 when the reversed integer overflows

        if x == 0:
            return 0
        else:
            signed = x / abs(x)
            string = str(abs(x))
            string = string[::-1]

            result = signed * int(string)
            
            if result >  2147483647 or result < -2147483648:
                return 0
            else:
                return result