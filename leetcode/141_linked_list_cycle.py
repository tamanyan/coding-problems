from typing import Dict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        id_map: Dict[int, bool] = {}
        cursor = head

        while cursor:
            cursor_id = id(cursor)
            if cursor_id in id_map:
                return True
            id_map[cursor_id] = True
            cursor = cursor.next

        return False
        