from typing import Dict, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        node_map: Dict[int, ListNode] = {}
        cursor = head

        while cursor:
            cursor_id = id(cursor)
            if cursor_id in node_map:
                return node_map[cursor_id]
            node_map[cursor_id] = cursor
            cursor = cursor.next
        
        return None
