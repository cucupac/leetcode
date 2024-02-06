from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # filter list
        if not head:
            return None

        # extract value list
        vals = self.extract_val(head=head)
        n = len(vals)

        # Rearrange list
        new_list = [0] * n

        for i, val in enumerate(vals):
            new_index = (i + k) % n
            new_list[new_index] = val

        # Construct linked list
        head = None
        for val in reversed(new_list):
            head = ListNode(val=val, next=head)
        return head

    def extract_val(self, head: Optional[ListNode]) -> List[int]:

        vals = []
        current = head
        while current.next:
            vals.append(current.val)
            current = current.next
        else:
            vals.append(current.val)

        return vals
