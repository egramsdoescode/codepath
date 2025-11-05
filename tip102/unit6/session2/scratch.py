class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def create_ll(values):
    if not values:
        return None
    dummy = Node(None)
    prev = dummy
    for value in values:
        prev.next = Node(value)
        prev = prev.next

    return dummy.next


# print_linked_list(create_ll([1, 2, 3, 4]))

head = create_ll([1, 2, 3, 5])


def insert_sorted(head, value):
    if not head:
        return Node(value)

    dummy = Node(None, head)
    prev = dummy

    curr = head
    while curr:
        if curr.value >= value:
            new_node = Node(value, prev.next)
            prev.next = new_node
            break
        prev = prev.next
        curr = curr.next

    return dummy.next


print_linked_list(insert_sorted(head, 6))
