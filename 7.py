class Solution(object):
    def reverse(self, x):
        flag = 0
        if x < 0:
            flag = 1
        x = (-1) ** flag * int(str(abs(x))[::-1])

        return x if -2 ** 31 <= x <= 2 ** 31 - 1 else 0

print(Solution().reverse(1534236469))
