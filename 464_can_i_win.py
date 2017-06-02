class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        # Winner is the one who make the total value >= desiredTotal
        # Can the first player force a win
        # eg: canIWin(10, 11) => false
