class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = res[i] 

#applied rotation via arithmetic operations, (i + k)% n does a full rotation of length(n) of the array
#Time Complexity O(n)
#Space Complexity O(n)