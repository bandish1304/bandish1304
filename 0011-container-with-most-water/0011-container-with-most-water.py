class Solution:
    def maxArea(self, height: List[int]) -> int:
        # first define all the pointers
        n = len(height)
        l = 0
        r = n-1
        max_area = 0

    # now we calculate area, height and width
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            a = w * h
            max_area = max(max_area, a)

    # And now we move left and right pointers
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area