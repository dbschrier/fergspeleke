class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r: #if they are the same, then it'll just stay in-place
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1