from linkedlist import Node

# すでにある要素をハッシュマップで記録しておけば良い。つまり


def remove_dups(ll):
    """
    llはlinkedlist(のつもりだが受け渡す**実体はあるNode**)
    """
    # llから見て何番目を削除するかのカウンター
    n = ll
    prev = None
    isunique = {}
    while n != None:
        if n.data in isunique.keys():
            prev.next = n.next
            # uniqueじゃなければprevを動かさない
        else:
            # uniqueだったらprevを一個ずれす
            prev = n
        isunique[n.data] = True

        n = n.next  # 次のnodeについて考える


if __name__ == "__main__":
    ls = Node(1)
    ls.appendToTail(2)
    ls.appendToTail(3)
    ls.appendToTail(5)  # opps
    ls.appendToTail(5)
    ls.appendToTail(6)
    ls.appendToTail(7)
    ls.appendToTail(2)  # opps
    ls.appendToTail(9)
    ls.appendToTail(10)
    ls.appendToTail(10)  # opps
    ls.appendToTail(2)  # opps
    ls.appendToTail(7)  # opps
    ls.printls()
    remove_dups(ls)
    ls.printls()
