class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            max_water = max(max_water, h * w)

            # move the smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water