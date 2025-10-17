class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we can do reverse and reverse in this one
        k = k % len(nums)
        l = 0
        r = len(nums) - 1

        # Now reverse the entire array
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # Now reverse again the first portion of the array
        l, r = 0, k -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # Now reverse second portion of the array
        l, r = k, len(nums) -1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        