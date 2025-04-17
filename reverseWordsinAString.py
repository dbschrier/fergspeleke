class Solution:
    def reverseWords(self, s: str) -> str:
        #here the goal is to point toward a length of characters such that it can
        #perform reverse, the algorithm scans across the string, implements reverse
        #stops when you reach the end of the string. return the string.

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        arr = list(s)  # Convert to list for in-place editing
        start = 0
        n = len(arr)

        for i in range(n + 1):  # Go one beyond to catch last word
            if i == n or arr[i] == ' ':
                reverse(arr, start, i - 1)
                start = i + 1  # Move past the space

        return ''.join(arr)