class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def inserting_of_a_node(self, data):
        node = Node(data)
        if not self.head:
            self.head =node
        else:
            node.next = self.head
            self.head = node

    def traverse(self):
        s=""
        current = self.head
        while current:
            s += str(current.data) + "->"
            current = current.next
        print(s)

    def deleting_the_linked_list(self):
        current_node = self.head
        print("*"*10)
        while current_node.next:
            del current_node.data
            current_node = current_node.next.next
            

if __name__ == '__main__':
    ll = LinkedList()
    print("*"*12)
    ll.inserting_of_a_node(1)
    ll.traverse()
    ll.inserting_of_a_node(1)
    ll.traverse()
    ll.inserting_of_a_node(3)
    ll.traverse()
    ll.inserting_of_a_node(4)
    ll.traverse()
    ll.inserting_of_a_node(5)
    ll.traverse()
    ll.deleting_the_linked_list()
    print("structure of the linked list after the delete the nodes")
    ll.traverse()

