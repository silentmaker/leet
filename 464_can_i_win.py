class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        # Winner is the one who make the total value >= desiredTotal
        # Can the first player force a win, eg: canIWin(10, 11) => false

        if maxChoosableInteger == 0:
            return False
        elif maxChoosableInteger == 1:
            return desiredTotal >= 1
        elif desiredTotal <= maxChoosableInteger or desiredTotal >= maxChoosableInteger + 2:
            return True
        else:
            return False
