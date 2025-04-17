class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [None] * n
        L = 0
        R = n - 1

        for i in range(n - 1, -1, -1):
            if nums[L] ** 2 > nums[R] ** 2:
                res[i] = nums[L] ** 2
                L += 1
            else:
                res[i] = nums[R] ** 2
                R -= 1
        return res
        #Time Complexity: O(n + however long sort() takes)
        #Space Complexity: O(n) because you create a new array squares.