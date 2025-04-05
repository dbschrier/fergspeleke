class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

#Time Complexity is O(n), since you at most have to traverse the array with n-elements.
#Space Complexity is O(n), since you have to allocate memory to hold uniquely n-elements.

