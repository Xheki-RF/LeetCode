from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1, lst2 = 0, 0
        g = 0
        while l1 != None:
            lst1 += l1.val * 10 ** g
            g += 1
            l1 = l1.next
        g = 0
        while l2 != None:
            lst2 += l2.val * 10 ** g
            g += 1
            l2 = l2.next

        line = tuple((int(x) for x in str(lst1 + lst2)))

        res = ListNode(line[0])

        for i in range(len(line)):
            if i == 0:
                res = ListNode(line[i])
            else:
                tmp = ListNode(line[i])
                tmp.next = res
                res = tmp

        return res

# List 1
a_1 = ListNode(2)
a_2 = ListNode(4)
a_3 = ListNode(3)
a_1.next = a_2
a_2.next = a_3

# List 2
b_1 = ListNode(5)
b_2 = ListNode(6)
b_3 = ListNode(4)
b_1.next = b_2
b_2.next = b_3

Solution().addTwoNumbers(a_1, b_1)
