from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # filter
        if not head:
            return None

        # extract vals
        vals = self.extract_vals(head=head)
        length = len(vals)

        vals.pop((length - 1) - (n - 1))

        # construct list
        head = None
        for val in reversed(vals):
            head = ListNode(val=val, next=head)

        return head

    def extract_vals(self, head: ListNode) -> List[int]:
        vals = []
        current = head
        while current.next:
            vals.append(current.val)
            current = current.next
        else:
            vals.append(current.val)

        return vals
