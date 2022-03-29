# Linked List Cycle II
# Question:

# Examples:
#


# O(n) - Time Complexity
# O(n) - Space Complexity
def detect_cycle(head):
    if head is None:
        return None
    cur_node = head
    seen_values = {cur_node}
    while cur_node.next is not None:
        if cur_node.next in seen_values:
            return cur_node.next
        seen_values.add(cur_node.next)
        cur_node = cur_node.next
    return None


# Floyd's Tortoise and Hare Algorithm
# O(n) - Time Complexity
# O(1) - Space Complexity
def detect_cycle_tortoise_and_hare(head):
    if head is None:
        return None
    tortoise = hare = head
    while True:
        if hare.next is None or hare.next.next is None:
            return None
        tortoise = tortoise.next
        hare = hare.next.next
        if hare == tortoise:
            break
    p1, p2 = head, hare
    while p1 != p2:
        p1, p2 = p1.next, p2.next
    return p1
