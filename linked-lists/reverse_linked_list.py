class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val


def print_linked_list(head):
    node = head
    nodes = []
    while node is not None:
        nodes.append(str(node.val))
        node = node.next
    nodes.append("None")
    return " --> ".join(nodes)


# O(n) - Time Complexity
# O(1) - Space Complexity
def reverse_linked_list_01(head):
    if head is None or head.next is None:
        return head
    first = head
    second = first.next
    first.next = None
    while second is not None:
        third = second.next
        second.next = first
        first = second
        second = third
    return first


# O(n) - Time Complexity
# O(1) - Space Complexity
def reverse_linked_list_02(head):
    prev = None
    cur_node = head
    while cur_node is not None:
        next_node = cur_node.next
        cur_node.next = prev
        prev = cur_node
        cur_node = next_node
    return prev


ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(print_linked_list(ll))
# print(print_linked_list(reverse_linked_list_01(ll)))
print(print_linked_list(reverse_linked_list_02(ll)))
