class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num-1 not in num_set:
                curr_num = num
                num_length = 1

                while curr_num + 1 in num_set:
                    num_length += 1
                    curr_num += 1
                longest = max(longest, num_length)

        return longest
        