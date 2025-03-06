class Solution(object):
    def largestCombination(self, candidates):
        max_len = 0

        for i in range(max(j.bit_length() for j in candidates)):
            x = 1 << i
            cnt = sum(1 for num in candidates if num & x)
            max_len = max(max_len, cnt)

        return max_len