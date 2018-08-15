"""
この問題が難しいのは、中間ノードだけ与えられたときにそれより前のノードが見えない点である。したがって中間ノードを削除するには中身自体を逐次書き換えなければいけない。
"""
from linkedlist import Node
from copy import deepcopy as copy


def remove_this_node(node):
    n = node
    while n.next != None:
        n.data = n.next.data
        # 終端処理、最後のノードを一個消す。
        if n.next.next == None:
            n.next = None
        else:
            # 終端じゃない場合は次のノードの処理に
            n = n.next


if __name__ == "__main__":
    ls = Node(1)
    ls.appendToTail(2)
    ls.appendToTail(3)
    ls.appendToTail(4)
    ls.appendToTail(5)
    ls.appendToTail(6)
    ls.appendToTail(7)
    ls.appendToTail(8)  # opps
    ls.appendToTail(9)
    ls.appendToTail(10)
    ls.printls()

    delnode = ls.get_Nth_node(5)
    remove_this_node(delnode)

    ls.printls()
