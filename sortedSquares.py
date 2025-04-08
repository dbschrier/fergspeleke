class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []

        for num in nums:
            square = num ** 2
            squares.append(square)

        squares.sort()
        return squares

        #Time Complexity: O(n + however long sort() takes)
        #Space Complexity: O(n) because you create a new array squares.