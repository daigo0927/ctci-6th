import os, sys
sys.path.append(os.pardir)
from utils.linkedlist import LinkedList

def search(llist):
    fast = llist.head
    slow = llist.head
    # Running until correlation
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        # loop absence
        return False
    fast = llist.head
    
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast
    


if __name__ == '__main__':
    # create looping linkedlist
    llist = LinkedList()
    llist.append_all([0, 9, 1, 8])
    loop_head = llist.tail
    llist.append_all([2, 4, 7, 3, 5, 6])
    llist.tail.next = loop_head
        
    n = llist.head
    for _ in range(15):
        if n is loop_head: print(str(n)+'(loop head)', end = ', ')
        else: print(str(n), end = ', ')
        n = n.next

    ans = search(llist)
    print(f'\nLoop head is {ans}.')
