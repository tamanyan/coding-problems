from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            tmpNext = cur.next
            cur.next = prev
            prev = cur
            cur = tmpNext
        
        return prev
