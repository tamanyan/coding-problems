# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # tmp
        sentinel = ListNode(0)
        sentinel.next = head
        prev = sentinel
        cursor = sentinel.next
        
        while cursor and cursor.next:
            # print("cursor:", cursor.val)
            # print("cursor next:", cursor.next.val)
            # print("prev:", prev.val)

            if cursor.val == cursor.next.val:
                val = cursor.val
                while cursor.next and val == cursor.next.val:
                    cursor = cursor.next
                prev.next = cursor.next
                cursor = cursor.next
            else:
                cursor = cursor.next
                prev = prev.next
        
        return sentinel.next

#         if head == None:
#             return None

#         current = head
#         ret_current = None
#         ret_head = None
#         duplicates = {}

#         while current != None:
#             if current.val in duplicates:
#                 current = current.next
#                 continue

#             if current.next != None and current.val == current.next.val:
#                 duplicates[current.val] = True
#                 current = current.next
#                 continue

#             if ret_head == None:
#                 ret_current = ret_head = ListNode(current.val)
#             else:
#                 ret_current.next = ListNode(current.val)
#                 ret_current = ret_current.next
                
#             current = current.next

#         return ret_head