class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first open empty hashmap
        seen = {}
        for i in range(len(nums)):
        # initate number to i
            num = nums[i]
        # if seen the number then return its index else add number to dictionary
            if target - num in seen:
                return [i, seen[target - num]]
            seen[num] = i
        