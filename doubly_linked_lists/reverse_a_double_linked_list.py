class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_head(self, data):
        node = Node(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node

        self.head = node


    def traverse(self):
        s=""
        current_node = self.head
        while current_node:
            s += str(current_node.data)+"=>"
            current_node = current_node.next
        print(s)

    def reverse_doubly_linked_list(self):
        current_node = self.head
        prev = None
        while current_node:
            if current_node.next == None:
                self.head = current_node
            prev = current_node.prev
            current_node.prev = current_node.next
            current_node.next=prev
            current_node = current_node.prev

if __name__ == '__main__':
    dll = DoublyLinkedList()

    for i in [74,65,566,5,7,29]:
        dll.insert_at_the_head(i)

    dll.traverse()
    dll.reverse_doubly_linked_list()
    dll.traverse()
    dll.reverse_doubly_linked_list()
    dll.traverse()