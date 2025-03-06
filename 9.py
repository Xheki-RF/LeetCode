class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False

print(Solution().isPalindrome(122))
