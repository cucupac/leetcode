# TODO: COME BACK AND SOLVE THIS AGAIN


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # List Checks
        if not list1 and not list2:
            return None

        if not list2 and list1:
            return list1

        if not list1 and list2:
            return list2

        # Extrct values
        sorted_values_1 = self.extractValues(list1)
        sorted_values_2 = self.extractValues(list2)

        merged_sorted = sorted(sorted_values_1 + sorted_values_2)

        # Construct a new sorted linked list
        head = None
        for value in reversed(merged_sorted):
            head = ListNode(val=value, next=head)

        return head

    def extractValues(self, list_node):
        values = []
        current = list_node
        while current:
            values.append(current.val)
            current = current.next
        return values
