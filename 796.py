from collections import deque

class Solution(object):
    def rotateString(self, s, goal):
        s_dq = deque(list(s))

        for i in range(len(goal)):
            s_dq.rotate(-1)

            if "".join(s_dq) == goal:
                return True

        return False