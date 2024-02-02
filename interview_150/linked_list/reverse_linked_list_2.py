from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # filter
        if not head:
            return None
        if head.next is None:
            return head

        # extract vals
        vals = []
        current = head
        while current.next:
            vals.append(current.val)
            current = current.next
        else:
            vals.append(current.val)

        # reverse subset
        vals[left - 1 : right] = reversed(vals[left - 1 : right])

        # reconstruct list
        head = None
        for val in reversed(vals):
            head = ListNode(val=val, next=head)

        return head


# Function to create a linked list from a list of values
def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head


# Create linked lists l1 and l2
head = create_linked_list([1, 2, 3, 4, 5])

solution = Solution()

solution.reverseBetween(head, 1, 1)
