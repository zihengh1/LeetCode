class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s) / 2)):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                swap(left + 1, right - 1)
        swap(0, len(s) - 1)

