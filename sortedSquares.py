class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        L = 0
        R = len(nums) - 1

        while L <= R:
            if nums[L] ** 2 > nums[R] ** 2:
                res.append(nums[L] ** 2)
                L += 1
            else:
                res.append(nums[R] ** 2)
                R -= 1
        return res[::-1]

        #Time Complexity: O(n)
        #Space Complexity: O(n) because you create a new array squares.