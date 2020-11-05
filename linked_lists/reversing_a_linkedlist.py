class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insert_a_node(self, data):
        node = Node(data)

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
            current_node = current_node.next

        print(s)

    def reversing_the_linked_list(self):
        next_node = None
        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node =current_node
            current_node = next_node
        self.head = prev_node




if __name__ == '__main__':
    ll = LinkedList()
    for i in [23, 34, 56, 7]:
        ll.insert_a_node(i)

    ll.traverse()
    ll.reversing_the_linked_list()
    ll.traverse()