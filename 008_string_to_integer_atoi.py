class Solution(object):
    def myAtoi(self, str):
        str = str.strip()
        is_digit = True
        digits = ['0','1','2','3','4','5','6','7','8','9']
        signs = ['+', '-']

        if len(str) == 0:
            return 0
        elif len(str) == 1:
            if str[0] in digits:
                return int(str[0])
            else:
                return 0
        elif len(str) > 1:
            if str[0] in signs or str[0] in digits:
                for i in range(len(str)):
                    if i == 0 or str[i] in digits:
                        continue
                    else:
                        i = i - 1
                        break
                if i == 0:
                    if str[0] in signs:
                        return 0
                    else:
                        return int(str[0])
                else:
                    if int(str[0:i + 1]) > 2147483647:
                        return 2147483647
                    elif int(str[0:i + 1]) < -2147483648:
                        return -2147483648
                    else:
                        return int(str[0:i + 1])
            else:
                return 0
        else:
            return 0