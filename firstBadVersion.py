# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n

        while L < R:
            mid = (L + R)//2 
            if isBadVersion(mid):
                R = mid
            else:
                L = mid + 1
        return L 

#Time Complexity: O(log2n), because the problem is iteratively sliced in half.
#Space Complexity: O(1), stores and checks finite variables in constant time. 