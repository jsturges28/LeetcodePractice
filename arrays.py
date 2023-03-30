def sortedSquares(nums: list[int]) -> list[int]:
        a = sorted(list(map(lambda x: x*x, nums)))
        return a

sortedSquares([-4,-1,0,3,10])