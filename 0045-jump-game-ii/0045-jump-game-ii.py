class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        far = 0
        end = 0

        for i in range(len(nums) -1):
            far = max(far, i+nums[i])
            if i == end:
                result += 1
                end = far
        return result

