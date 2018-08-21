import linkedlist2 as ll2

def is_palindrome(llist):
    # runner technique, method2
    fast = llist.head
    slow = llist.head
    stack = []
    while fast is not None and fast.next is not None:
        stack.append(slow.value)
        fast = fast.next.next
        slow = slow.next

    if fast is not None:
        # when the llist length is odd, skip the meddle node
        slow = slow.next

    while slow is not None:
        if stack[-1] != slow.value:
            return False
        else:
            stack = stack[:-1]
            slow = slow.next
    return True

if __name__ == '__main__':
    cases = [[1, 2, 3, 2, 1],
             [1, 2, 5, 2, 4],
             [1,1, 2, 2, 1, 1]]
    
    for case in cases:
        llist = ll2.LinkedList()
        llist.append_all(case)
        ans = is_palindrome(llist)
        print(f'{str(llist)} is palindrome? : {ans}')

        
