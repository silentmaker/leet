class Solution(object):
    def isMatch(self, s, p):
        if '*' not in p and '.' not in p:
            if p != s:
                return False
            else:
                return True
        elif '*' not in p and '.' in p:
            if len(s) == len(p):
                for i in range(len(s)):
                    if p[i] != '.' and s[i] != p[i]:
                        return False
                    else:
                        return True
            else:
                return False
        else:
            j = 0
            good_p = ''
            for i in range(len(p)):
                if i >= 2 and i + 1 <= len(p):
                    if p[i - 1] == '*' and p[i - 2] == p[i]:
                        continue
                good_p = good_p + p[i]
            p = good_p

            for i in range(len(s)):
                if j >= len(p):
                    return False
                elif s[i] != p[j]:
                    if p[j] == '.':
                        j = j + 1
                    elif p[j] == '*':
                        if j >= 1 and (p[j - 1] == '.' or p[j - 1] == s[i]):
                            continue
                        elif j + 1 < len(p) and (p[j + 1] == '.' or p[j + 1] == s[i]):
                            j = j + 2
                    elif j + 2 < len(p) and p[j + 1] == '*' and p[j + 2] == s[i]:
                        j = j + 3
                    else:
                        return False
                else:
                    j = j + 1

            if j < len(p):
                for i in range(j + 1, len(p)):
                    if p[i] != '*':
                        if i + 1 < len(p) and p[i + 1] == '*':
                            continue
                        elif i + 1 == len(p) and len(s) > 0 and p[i] == s[-1]:
                            continue
                        else:
                            return False
                return True
            else: 
                return True