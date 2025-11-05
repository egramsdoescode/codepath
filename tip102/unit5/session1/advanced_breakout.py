class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.value, end=" -> " if curr.next else "\n")
        curr = curr.next


# 1

"""
U: 
- input: Head of a singly linked list of nodes with integers as values
- output: Maximum value of all of the nodes in the linked list

Ex. input: 1 -> 8 -> 2
Ex. output: 8 

M: Single traversal with one pointer, no other pointers needed

P: Create a maximum variable, set to negative inf. Using a curr pointer, start at the head and iterate through the list, comparing the curr node's value to the maximum variable, if it is higher than the curr max, update max to be the value of the curr node. Return the highest value after one full pass of the ll

E: O(n) time, O(1) space 


"""


def find_max(head):
    if not head:
        return None
    maximum_val = float("-inf")
    curr = head
    while curr:
        # This is to account for nodes with values that are non-numeric
        if isinstance(curr.value, (int, float)) and curr.value > maximum_val:
            maximum_val = curr.value
        curr = curr.next
    return maximum_val


print("--- Problem 1 ---")
head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))

head3 = Node(5, Node("Pikachu", Node(6, Node(7))))

print(find_max(head3))

# 2

"""
U: 
- input: head of a singly linked list with strings as values
- output: head of modified singly linked list, where the tail has been removed.

DEFINITION: Tail is the last node of a linked list.

Ex. input: "Joseph" -> "Carrie" -> "Ethan" ->
Ex. output: "Joseph" -> "Carrie" ->  

M: Single traversal of the linked list, no extra pointers 

P: Traverse the linked list until we get to the SECOND to last node, point the second to last node's next pointer to None, return head of the modified list


"""


def remove_tail(head):
    if not head and not head.next:
        return None

    curr = head
    while curr.next.next:
        curr = curr.next

    curr.next = None
    return head


print("\n--- Problem 2 ---")
head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

# 3
"""
U: Given a sorted ll, implement a funtion that removes any node with an integer value that is repeated in the ll, including the first occurence

- input: head of a singly linked list of integers
- output: head of the modified list

Ex. input: 1 -> 2 -> 3 -> 3 -> 4 -> 5->
Ex. output: 1 -> 2 -> 4 -> 5 ->   

M: Two pointer technique?? Or create an extra space list

P: Start with a left and right pointer at the same place. 


"""


def delete_dupes(head):
    if not head:
        return None
    if not head.next:
        return head

    dummy = Node(None, head)
    prev = dummy
    curr = head

    while curr:
        saw_duplicate = False
        while curr.next and curr.value == curr.next.value:
            curr = curr.next
            saw_duplicate = True

        if saw_duplicate:
            prev.next = curr.next
        else:
            prev = prev.next

        curr = curr.next

    return dummy.next


print("\n--- Problem 3 ---")


head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))
