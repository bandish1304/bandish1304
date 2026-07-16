class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # first we define i and j float of inf. is the smallest
        nums_i = float('inf')
        nums_j = float('inf')
        # we have to make sure that i < j and if 
        # next number after j is greater than return true
        for num in nums:
            if num <= nums_i:
                nums_i = num
        # And if it's not smaller than make that number j
            elif num <= nums_j:
                nums_j = num
        # And if that number is bigger than i and j then make k
            else:
                return True
        return False
