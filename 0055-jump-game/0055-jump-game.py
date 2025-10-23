class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1

        for i in range(n-1, -1, -1):
            # first make a variable of max_jump
            max_jump = nums[i]
            if max_jump + i >= target:
                target = i

        return target == 0
        