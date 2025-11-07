class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        # now put the index in the hashmap
        for i in range(len(nums)):
            h[nums[i]] = i

        # now use the formula y = y-x
        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y] != i:
                return[i, h[y]]