class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest = 0
        n = len(nums)
        end = 0
        farthest = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                smallest += 1
                end = farthest

        return smallest