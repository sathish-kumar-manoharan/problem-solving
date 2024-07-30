
from linked_list.ListNode import ListNode

def remove_even_values(head):
    dummy = ListNode(-1)
    dummy.next = head

    current = dummy

    while current is not None:
        if current.next and current.next.value %2 == 0:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next

def print_linked_list(head):
    current = head

    while current:
        print(current)
        current = current.next

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
seven = ListNode(7)
eight = ListNode(8)
nine = ListNode(9)
ten = ListNode(10)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine
nine.next = ten

print("Before removing even numbers")
print_linked_list(one)
print("After removing even numbers")
print_linked_list(remove_even_values(one))
