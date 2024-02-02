from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Adds two numbers stored in linked list together and returns the result."""

        # filter
        self.filter_lists(l1=l1, l2=l2)

        # extract vals
        l1_vals = self.extract_values(head=l1)
        l2_vals = self.extract_values(head=l2)

        # sum numbers
        num_1 = int("".join(map(str, reversed(l1_vals))))
        num_2 = int("".join(map(str, reversed(l2_vals))))

        print("num_1:", num_1)
        print("num_2:", num_2)

        result_str = reversed(str(num_1 + num_2))

        # convert back to list
        result = [int(char) for char in result_str]

        print(result)

        # constuct linked list
        next_node = None
        current_node = None
        for val in reversed(result):
            current_node = ListNode(val=val, next=next_node)
            next_node = current_node

        return current_node

    def extract_values(self, head: Optional[ListNode]) -> List[int]:
        """Convert linked list values into list of integers."""
        vals = []
        current_node = head
        while current_node.next:
            vals.append(current_node.val)
            current_node = current_node.next
        else:
            vals.append(current_node.val)

        return vals

    def filter_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> None:
        """Filter list."""
        if l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        elif not l1 and not l2:
            return None


# Function to create a linked list from a list of values
def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head


# Create linked lists l1 and l2
l1 = create_linked_list([2, 4, 9])
l2 = create_linked_list([5, 6, 4, 9])

solution = Solution()

solution.addTwoNumbers(l1, l2)
