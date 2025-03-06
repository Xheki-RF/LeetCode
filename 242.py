class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        dict_s, dict_t = {i: s.count(i) for i in set(s)}, {
            j: t.count(j) for j in set(t)
        }

        return [False, True][dict_s == dict_t]