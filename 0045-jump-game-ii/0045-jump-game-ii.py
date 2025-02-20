class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest = 0
        n = len(nums)
        far = 0
        end = 0

        for i in range(n-1):
            far = max(far, i +nums[i])
            if i == end:
                smallest += 1
                end = far

        return smallest
        