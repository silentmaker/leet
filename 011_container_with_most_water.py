# time limit exceeded
class Solution(object):
    def maxArea(self, height):
        water = 0;
        for i in range(0, len(height)):
            if id > 0 and height[i] < height[i - 1]:
                continue
            for j in range(i,len(height)):
                tmp = min(height[i], height[j]) * (j - i)
                if water < tmp:
                    water = tmp
        
        return water