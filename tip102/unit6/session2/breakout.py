class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def partition(suspect_ratings, threshold):
    greater_dummy = Node(None)
    lesser_dummy = Node(None)

    greater_tail = greater_dummy
    lesser_tail = lesser_dummy

    curr = suspect_ratings
    while curr:
        next_node = curr.next
        curr.next = None
        if curr.value > threshold:
            greater_tail.next = curr
            greater_tail = greater_tail.next
        else:
            lesser_tail.next = curr
            lesser_tail = lesser_tail.next

        curr = next_node

    greater_tail.next = lesser_dummy.next
    return greater_dummy.next


print("--- Problem 3 ---")
suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))


def merge_timelines(known_timeline, witness_timeline):
    dummy = Node(None)
    merged_tail = dummy

    known_curr = known_timeline
    witness_curr = witness_timeline

    while known_curr and witness_curr:
        known_next_node = known_curr.next
        witness_next_node = witness_curr.next

        if witness_curr.value <= known_curr.value:
            witness_curr.next = None
            merged_tail.next = witness_curr
            merged_tail = merged_tail.next
            witness_curr = witness_next_node
        else:
            known_curr.next = None
            merged_tail.next = known_curr
            merged_tail = merged_tail.next
            known_curr = known_next_node

    merged_tail.next = known_curr or witness_curr

    return dummy.next


print("\n--- Problem 4 ---")
known_timeline = Node(1, Node(2, Node(4, Node(6))))
witness_timeline = Node(1, Node(3, Node(4, Node(5))))
print_linked_list(merge_timelines(known_timeline, witness_timeline))


def rotate_right(evidence, k):
    head = evidence
    if not head or not head.next or k == 0:
        return head

    def find_length_and_tail(node):
        length = 1
        curr = node
        while curr.next:
            curr = curr.next
            length += 1
        return length, curr

    length, tail = find_length_and_tail(head)

    k %= length
    if k == 0:
        return head

    tail.next = head

    steps_to_new_tail = length - k - 1
    new_tail = head

    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


print("\n--- Problem 5 ---")
evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))

print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))

print("\n--- Problem 6 ---")


def add_two_numbers(head_a, head_b):
    num_a = []
    num_b = []

    curr = head_a
    while curr:
        num_a.append(str(curr.value))
        curr = curr.next

    num_a = "".join(num_a)

    curr = head_b
    while curr:
        num_b.append(str(curr.value))
        curr = curr.next

    num_b = "".join(num_b)

    num_a = num_a[::-1]
    num_b = num_b[::-1]

    sum_str = str(int(num_a) + int(num_b))

    def sum_ll(sum_str):
        dummy = Node(None)
        prev = dummy
        for i in range(len(sum_str) - 1, -1, -1):
            prev.next = Node(int(sum_str[i]))
            prev = prev.next
        return dummy.next

    return sum_ll(sum_str)


head_a = Node(2, Node(4, Node(3)))  # 342
head_b = Node(5, Node(6, Node(4)))  # 465
print_linked_list(add_two_numbers(head_a, head_b))
