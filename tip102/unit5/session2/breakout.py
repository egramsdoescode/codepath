class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_ll(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


print("--- Problem 4 ---")


def halve_list(head):
    new_head = head
    while head:
        head.value /= 2
        head = head.next

    return new_head


node_one = SinglyNode(5)
node_two = SinglyNode(6)
node_three = SinglyNode(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_ll(halve_list(node_one))

print("\n--- Problem 5 ---")


def delete_tail(head):
    new_head = head
    curr = head

    # traverse list unitl at second-to-last node
    while curr.next.next:
        curr = curr.next

    curr.next = None
    return new_head


butterfly = SinglyNode("Common Butterfly")
ladybug = SinglyNode("Ladybug")
beetle = SinglyNode("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_ll(delete_tail(butterfly))

print("\n--- Problem 6 ---")


def find_min(head):
    minimum_val = float("inf")
    curr = head
    while curr:
        if curr.value < minimum_val:
            minimum_val = curr.value
        curr = curr.next

    return minimum_val


head1 = SinglyNode(5, SinglyNode(6, SinglyNode(7, SinglyNode(8))))
head2 = SinglyNode(8, SinglyNode(5, SinglyNode(6, SinglyNode(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))

print("\n--- Problem 7 ---")


def delete_item(head, item):
    if head.value == item:
        new_head = head.next
        head.next = None
        return new_head

    new_head = head
    curr = head
    while curr.next.next:
        if curr.next.value == item:
            curr.next = curr.next.next
            break
        curr = curr.next
    return new_head


slingshot = SinglyNode("Slingshot")
peaches = SinglyNode("Peaches")
beetle = SinglyNode("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_ll(delete_item(slingshot, "Slingshot"))

# Reset linked list values
slingshot = SinglyNode("Slingshot")
peaches = SinglyNode("Peaches")
beetle = SinglyNode("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

print_ll(delete_item(slingshot, "Peaches"))
print_ll(delete_item(slingshot, "Triceratops Torso"))

print("\n--- Problem 8 ---")


def tail_to_head(head):
    if not head or not head.next:
        return

    curr = head

    while curr.next.next:
        curr = curr.next

    new_head = curr.next
    new_head.next = head
    curr.next = None
    return new_head


daisy = SinglyNode("Daisy")
mario = SinglyNode("Mario")
toad = SinglyNode("Toad")
peach = SinglyNode("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

single_node_ll = SinglyNode("single")

# Linked List: Daisy -> Mario -> Toad -> Peach
print_ll(tail_to_head(daisy))

print("\n--- Problem 9 ---")


class DoublyNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


head = DoublyNode("Isabelle")
tail = DoublyNode("K.K. Slider")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)

print("\n--- Problem 10 ---")


def print_reverse(tail):
    curr = tail
    while curr:
        print(curr.value)
        curr = curr.prev


isabelle = DoublyNode("Isabelle")
kk_slider = DoublyNode("K.K. Slider")
saharah = DoublyNode("Saharah")
isabelle.next = kk_slider
kk_slider.next = saharah
saharah.prev = kk_slider
kk_slider.prev = isabelle

# Linked List: Isabelle <-> K.K. Slider <-> Saharah
print_reverse(saharah)
