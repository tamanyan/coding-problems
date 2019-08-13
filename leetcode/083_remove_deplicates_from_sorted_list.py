import string
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        fake = ListNode(0)
        fake.next = head
        prev = fake
        cursor = fake.next
        
        while cursor and cursor.next:
            if cursor.val == cursor.next.val:
                val = cursor.val
                while cursor.next and val == cursor.next.val:
                    cursor = cursor.next
                prev.next = cursor
            cursor = cursor.next
            prev = prev.next
            
        return fake.next
            
                
#         if head == None:
#             return None

#         duplicates = {}
#         new_head = ListNode(head.val)
#         duplicates[head.val] = True
#         cursor = head
#         new_cursor = new_head
        
#         while cursor != None:
#             if cursor.val in duplicates:
#                 cursor = cursor.next
#                 continue

#             duplicates[cursor.val] = True
#             tmp = ListNode(cursor.val)
#             new_cursor.next = tmp
#             new_cursor = new_cursor.next
#             cursor = cursor.next
        
#         return new_head
        