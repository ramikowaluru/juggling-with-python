class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_a_node_into_linkedlist(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
             node.next = self.head
             self.head = node


    def traverse(self):
        s = ""
        curtrent_node = self.head
        while curtrent_node:
            s += str(curtrent_node.data)+"->"
            curtrent_node = curtrent_node.next

        print(s)

    def detecting_loop(self):
        fast_ref = self.head
        slow_ref = self.head
        while fast_ref:
            fast_ref = fast_ref.next.next
            slow_ref = slow_ref.next
            if fast_ref == slow_ref:
                return "There is a loop"
                break

        return "There is no loop"


if __name__ == '__main__':
    ll = LinkedList()
    lelements = [1, 2,"er",34,"sdaf",345]


    for i in lelements:
        ll.insert_a_node_into_linkedlist(i)
    ll.traverse()
    print(ll.detecting_loop())
    ll.head.next.next.next.next.next.next = ll.head.next
    print(ll.detecting_loop())