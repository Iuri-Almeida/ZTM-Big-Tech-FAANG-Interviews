# M, N Reversals
# Question: Given a Linked List and numbers m and n, return it back with only positions m to n in reverse.

# Examples:
# ll = 1 → 2 → 3 → 4 → 5, m = 2, n = 4:  1 → 4 → 3 → 2 → 5
# ll = 1 → 4 → 5 → 9 → 11 → 13, m = 1, n = 9:  9 → 5 → 4 → 1 → 11 → 13
# ll = 1 → 2 → 3 → 4 → 5, m = 1, n = 5:  5 → 4 → 3 → 2 → 1
# ll = 5, m = 1, n = 1 → 5
# ll = null, m = 0, n = 0, null


class ListNode(object):
    def __init__(self, val=0, next=None):
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
def reverse_linked_list(start, end):
    prev = None
    cur_node = start
    tail = cur_node
    while cur_node != end:
        next_node = cur_node.next
        cur_node.next = prev
        prev = cur_node
        cur_node = next_node
    cur_node.next = prev
    prev = cur_node
    return prev, tail


# O(n) - Time Complexity
# O(1) - Space Complexity
def m_n_reversals(head, left, right):
    if head is None or head.next is None or left == right:
        return head

    cur_node = head
    node_before = node_left = None

    for i in range(1, right):

        if i == left - 1:
            node_before = cur_node

        if i == left:
            node_left = cur_node

        cur_node = cur_node.next

    node_after = cur_node.next
    start, end = reverse_linked_list(node_left, cur_node)
    end.next = node_after

    # check if left is point to head (if so, we do not have any before node!)
    if left - 1 == 0:
        return start

    node_before.next = start
    return head


ll = ListNode(8, ListNode(7, ListNode(6, ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))))
print(print_linked_list(ll))
print(print_linked_list(m_n_reversals(ll, 2, 4)))
