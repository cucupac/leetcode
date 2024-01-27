# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import defaultdict
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            # Cycle not possible if no nodes
            return False

        nodes = defaultdict(bool)
        current_node: ListNode = head
        while True:
            if current_node.next is None:
                # We made it to the end and there's no next -> no cycle
                return False

            if nodes.get(current_node.next):
                # It points to an already traversed node -> cycle
                return True

            # Update node storage
            nodes[current_node] = True
            current_node = current_node.next
