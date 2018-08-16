from linkedlist import Node as _Node

# 愚直に最後まで数える方法


class Node(_Node):
    def show_Kth_to_last(self, K):
        lencount = 0
        n = self
        # 一番終端のノードまで移動する回数がつまりリストの長さ。
        while (n.next != None):
            lencount += 1
            n = n.next

        #後ろからK番目はつまりlencount - K番目
        # 後ろから0番目を最後のノードだと定義して

        print(self.get_Nth_node(lencount - K).data)


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
    ls.show_Kth_to_last(0)
    ls.show_Kth_to_last(3)
    ls.show_Kth_to_last(12)
    ls.show_Kth_to_last(-3)
