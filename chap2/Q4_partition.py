"""
大小比較して前半のリストと後半のリストをべっこに作り後から連結すれば良い
"""
from linkedlist import Node


def partation(ll, K):
    """
    Kの大きさで分割して並び替えたものを返す。
    """
    n = ll
    left, right = Node(), Node()
    while True:
        if n.data < K:
            left.appendToTail(n.data)
        else:
            right.appendToTail(n.data)
        if n.next == None:
            break
        n = n.next

    # これだと宣言の関係上一番始めがNoneになっているのでとりのぞいてから連結する
    right = right.get_Nth_node(1)
    left = left.get_Nth_node(1)
    left.appendNodeToTail(right)
    return left


if __name__ == "__main__":
    ls = Node(1)
    ls.appendToTail(10)
    ls.appendToTail(3)
    ls.appendToTail(4)
    ls.appendToTail(5)
    ls.appendToTail(6)
    ls.appendToTail(5)
    ls.appendToTail(8)
    ls.appendToTail(9)
    ls.appendToTail(10)
    ls.printls()

    new = partation(ls, 5)
    new.printls()
