import os, sys
sys.path.append(os.pardir)
from utils.linkedlist import Node, LinkedList


def is_shared(llist_1, llist_2):
    if llist_1.tail is not llist_2.tail:
        return False
    
    n1, n2 = llist_1.head, llist_2.head
    if len(llist_1) > len(llist_2):
        for _ in range(len(llist_1) - len(llist_2)):
            n1 = n1.next
    elif len(llist_2) > len(llist_1):
        for _ in range(len(llist_2) - len(llist_1)):
            n2 = n2.next

    while n1 is not None and n2 is not None:
        if n1 is n2:
            return n1
        n1 = n1.next
        n2 = n2.next


if __name__ == '__main__':
    # case1
    llist_1, llist_2 = LinkedList(), LinkedList()
    llist_1.append_all([3, 1, 5, 9])
    llist_2.append_all([4, 6])
    for v in [7, 2, 1]:
        tail_new = Node(v)
        llist_1.tail.next = tail_new
        llist_1.tail = tail_new
        llist_2.tail.next = tail_new
        llist_2.tail = tail_new
    ans = is_shared(llist_1, llist_2)
    print(f'{str(llist_1)} and {str(llist_2)} share? {ans}')

    llist_1, llist_2 = LinkedList(), LinkedList()
    llist_1.append_all([3, 1, 5, 9, 7, 2, 1])
    llist_2.append_all([4, 6, 7, 2, 1])
    ans = is_shared(llist_1, llist_2)
    print(f'{str(llist_1)} and {str(llist_2)} share? {ans}')
