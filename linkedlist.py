class Node:
    """
    import linkedlistがなぜかimportできないので、自分で書く
    """

    def __init__(self, d=None):
        self.data = d
        self.next = None  # odeを受け渡すようにすると多分ポインター参照になるらし

    def appendToTail(self, d):
        end = Node(d)  # あたらしいノード
        n = self
        # 一番終端のノードまで移動する必要がある。
        while (n.next != None):
            n = n.next
        n.next = end

    def printls(self):
        n = self
        while(1):
            if n.next == None:
                print(n.data)
                break
            print(n.data, end=", ")
            n = n.next

    def get_Nth_node(self, N):
        """
        配列ライクにN番目のノードを返す(データではない)
        """
        n = self
        for _ in range(N):
            if n.next == None:
                print("Index out of bound. return the last node")
                break
            n = n.next
        return n

    def remove_Nth_node(self, N):
        if N == 0:
            self = self.next

        prerm = self.get_Nth_node(N - 1)  # 削除したいノードの一つ前のリンクを書き換える必要がある
        prerm.next = self.get_Nth_node(N).next
        #. -> . ->(この矢印を書き換える必要がある) .(削除したい) -> .


if __name__ == "__main__":

    nd = Node(1)
    nd.appendToTail(3)
    nd.appendToTail(5)
    nd.appendToTail(7)
    nd.appendToTail(9)

    nd.printls()
    print(nd.get_Nth_node(3).data)
    print(nd.get_Nth_node(4).data)
    print(nd.get_Nth_node(5).data)

    nd.remove_Nth_node(3)
    nd.printls()
