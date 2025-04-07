class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R)//2 
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        return R + 1
    
    #Time Complexity: O(log2n), slicing the problem set in half
    #Space Complexity: O(1), since we're only checking finite variables which is constant. 