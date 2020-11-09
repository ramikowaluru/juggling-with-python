class Node:
    def __init__(self,data, next=None, prev=None):
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
            s +=str(current_node.data)+"->"
            current_node = current_node.next
        print(s)

    def delete_a_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                # is it the tail
                if current_node.next:
                    temp = current_node.prev
                    # is it not the head
                    if current_node.prev:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = temp
                    else:
                        self.head = self.head.next
                        self.head.prev = None
                else:
                    current_node.prev.next = None
                break
            current_node = current_node.next


if __name__ == '__main__':
    dll = DoublyLinkedList()

    for i in [23,12,5,55,6,7]:
        dll.insert_at_the_head(i)
    dll.traverse()
    dll.insert_at_the_head(2340)
    dll.traverse()
    dll.delete_a_node(2340)
    dll.traverse()
    dll.insert_at_the_head("head")
    dll.traverse()