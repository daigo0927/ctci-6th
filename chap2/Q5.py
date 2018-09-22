import os, sys
sys.path.append(os.pardir)
from utils.linkedlist import LinkedList


def solve(llist_1, llist_2):
    n1, n2 = llist_1.head, llist_2.head
    llist_ans = LinkedList()
    carry = 0
    while n1 is not None or n2 is not None:
        result = carry
        if n1 is not None:
            result += n1.value
            n1 = n1.next
        if n2 is not None:
            result += n2.value
            n2 = n2.next

        llist_ans.append(result%10)
        carry = result//10

    if carry > 0:
        llist_ans.append(carry)

    print(f'{str(llist_1)} + {str(llist_2)} = {llist_ans}')

def solve2(llist_1, llist_2):
    if len(llist_1) > len(llist_2):
        for _ in range(len(llist_1) - len(llist_2)):
            llist_2.pad_head()
    elif len(llist_2) > len(llist_1):
        for _ in range(len(llist_2) - len(llist_1)):
            llist_1.pad_head()

    n1, n2 = llist_1.head, llist_2.head
    llist_ans = LinkedList()
    result = 0
    while n1 is not None and n2 is not None:
        result = 10*result+n1.value+n2.value
        n1 = n1.next
        n2 = n2.next

    for v in str(result):
        llist_ans.append(int(v))

    print(f'{str(llist_1)} + {str(llist_2)} = {llist_ans}')


if __name__ == '__main__':
    llist_1, llist_2 = LinkedList(), LinkedList()
    llist_1.append_all([7, 1, 6])
    llist_2.append_all([5, 9, 2])
    solve(llist_1, llist_2)

    llist_1, llist_2 = LinkedList(), LinkedList()
    llist_1.append_all([1, 2, 3, 4])
    llist_2.append_all([5, 6, 7])
    solve2(llist_1, llist_2)

    
