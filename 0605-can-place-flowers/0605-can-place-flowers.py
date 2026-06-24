class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # first check if n == 0
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            # define the variable to check whether left and right are zero
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed)- 1) or flowerbed[i+1] == 0
            # if both conditions are true then check flowerbed[i] == 0
            # and if yes the replace that with 1
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False

        