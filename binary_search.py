class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R)//2
            if target == mid:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            else:
                R = mid - 1
        return -1 #could not be found

        #Time Complexity is log2(n), cutting the problem in half each time
        #Space Complexity is O(n), comparisons are done in constant time.