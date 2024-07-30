from linked_list.LinkedList import LinkedList

def remove_even_values(head):
    dummy = LinkedList(-1)
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

one = LinkedList(1)
two = LinkedList(2)
three = LinkedList(3)
four = LinkedList(4)
five = LinkedList(5)
six = LinkedList(6)
seven = LinkedList(7)
eight = LinkedList(8)
nine = LinkedList(9)
ten = LinkedList(10)

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
