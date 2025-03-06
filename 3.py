class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0

        seen = {}
        left = 0
        max_length = 0

        for right in range(n):
            # If character s[right] is already seen, move the left pointer
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            # Update the latest index of the character
            seen[s[right]] = right
            # Calculate the max length so far
            max_length = max(max_length, right - left + 1)

        return max_length


print(Solution().lengthOfLongestSubstring("eww"))
