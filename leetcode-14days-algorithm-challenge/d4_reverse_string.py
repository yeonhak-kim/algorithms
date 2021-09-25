# Reverse String
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # space O(1) solution. However, in a situation where operation speed is in higher priority, better convert string to array of char and perform index swaps.
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1