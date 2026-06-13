class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # first we have to find max number in candies
        greatest = max(candies)
        # then we need to initiate output/result to an empty array
        result = []
        # and now do for loop and if else statement
        for candy in candies:
            if candy + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
        