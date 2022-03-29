# Flatten Multi Level Doubly Linked List
# Question: Given a doubly linked list, list nodes also have a child property that can point to a separate doubly
# linked list. These child lists can also have one or more child  doubly linked lists of their own, and so on. Return
# the list as a single level flattened doubly linked list.

# Examples:
# 1 <-> 2 <-> 3 <-> 4 <-> 5
#                   |
#                   6 <-> 7 <-> 8
#                         |
#                         9 <-> 10
#
# 1
# |
# 2
# |
# 3


def flatten(head):
    __flatten_recursive(head)
    return head


# O(n) - Time Complexity
# O(n) - Space Complexity
def __flatten_recursive(node):
    if node is None:
        return node
    cur_node = node
    while cur_node.next is not None or cur_node.child is not None:
        if cur_node.child is not None:
            # child -> cur_node
            cur_node.child.prev = cur_node
            # last child reference
            last_child_node = __flatten_recursive(cur_node.child)
            # next node reference
            next_node = cur_node.next
            # cur_node -> child
            cur_node.next = cur_node.child
            # last child <--> next_node
            last_child_node.next = next_node
            if next_node is not None:
                next_node.prev = last_child_node
            # cur_node.child -> None
            cur_node.child = None
        cur_node = cur_node.next
    return cur_node


# O(n) - Time Complexity
# O(1) - Space Complexity
def flatten__iterative(head):
    if head is None:
        return head
    cur_node = head
    while cur_node.next is not None or cur_node.child is not None:
        if cur_node.child is not None:
            # child -> cur_node
            cur_node.child.prev = cur_node
            # last child reference
            last_child_node = cur_node.child
            while last_child_node.next is not None:
                last_child_node = last_child_node.next
            # next node reference
            next_node = cur_node.next
            # cur_node -> child
            cur_node.next = cur_node.child
            # last child <--> next_node
            last_child_node.next = next_node
            if next_node is not None:
                next_node.prev = last_child_node
            # cur_node.child -> None
            cur_node.child = None
        cur_node = cur_node.next
    return head
