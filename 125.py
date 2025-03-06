class Solution(object):
    def isPalindrome(self, s):
        new_s = "".join(filter(lambda i: i.isalnum(), s.lower()))

        if new_s == new_s[::-1]:
            return True
        else:
            return False