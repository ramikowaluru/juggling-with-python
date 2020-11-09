class Node:
    def __init__(self, data, prev=None, next = None):
        self.data = data
        self.prev = prev
        self.next = next



class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_head(self, data):
        node = Node(data=data)
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev = node

        self.head = node

    def insert_after_a_particular_node(self, prev_node, data):
        node =Node(data)
        node.next = prev_node.next
        prev_node.next = node
        node.prev = prev_node


    def insert_at_the_end(self, data):
        node = Node(data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        node.prev = current_node
        current_node.next = node


    def traverse(self):
        s=""
        current_node = self.head
        while current_node:
            s += str(current_node.data)+"->"

            current_node = current_node.next
        print(s)

if __name__ == '__main__':
    dll = DoubleLinkedList()
    for i in ['a',1,3,'d',10]:
        dll.insert_at_the_head(i)
    dll.traverse()
    dll.insert_at_the_end(123)
    dll.insert_at_the_end("adf")
    dll.traverse()