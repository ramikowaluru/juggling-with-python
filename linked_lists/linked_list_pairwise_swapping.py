class Node:
    def __init__(self, data):
        self.data =data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_a_node(self, data):
        node  = Node(data)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def traverse(self):
        s = ""
        current_node = self.head
        while current_node:
            s += str(current_node.data)+"->"
            current_node  = current_node.next

        print(s)

    def pairwise_swapping(self):
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node.data, current_node.next.data = current_node.next.data, current_node.data
            current_node = current_node.next.next


if __name__ == '__main__':
    ll = LinkedList()
    for i in [1,2,3,4,5,6,7]:
        ll.insert_a_node(i)
    ll.traverse()
    ll.pairwise_swapping()
    ll.traverse()