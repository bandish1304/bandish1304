class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # so first define both nums1 and nums2 as set
        nums1 = set(nums1)
        nums2 = set(nums2)
        # Then we initialize nums1 answer to fill numbers from set
        ans1 = []
        # now we do for loop
        for num in nums1:
            if num not in nums2:
                ans1.append(num)
            else:
                nums2.remove(num)
        return[ans1, list(nums2)]