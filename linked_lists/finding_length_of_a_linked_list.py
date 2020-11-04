class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_a_node(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def get_the_length_of_linked_list(self):
        current_node = self.head
        n=0
        while current_node:
            current_node=current_node.next
            n += 1
        return n


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_a_node(1)
    ll.insert_a_node(2)
    ll.insert_a_node(3)
    ll.insert_a_node(3)
    ll.insert_a_node(4)
    print(ll.get_the_length_of_linked_list())