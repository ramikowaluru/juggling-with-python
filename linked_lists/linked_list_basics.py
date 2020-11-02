class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def inset_data(self, data):
        self.numOfNodes += 1
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.nextNode = self.head
            self.head = node

    def insert_end(self, data):
        self.numOfNodes += 1
        node = Node(data)
        actual_node = self.head
        while actual_node.nextNode:
            actual_node = actual_node.nextNode
        actual_node.nextNode = node

    def print_linked_list(self):
        curr = self.head
        while curr:
            print(curr.data, "->", end="")
            curr = curr.nextNode

    def size_of_the_linked_list(self):
        return self.numOfNodes

    def remove(self, data):
        if self.head is None:
            return
        actual_node = self.head
        previous_node = None
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.nextNode
            self.numOfNodes -= 1
        else:
            previous_node.nextNode = actual_node.nextNode
            self.numOfNodes -= 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.inset_data(1)
    ll.inset_data(3)
    ll.inset_data(5)
    ll.inset_data(9)
    ll.insert_end(10)
    ll.print_linked_list()
    print()
    print("size before removal", ll.numOfNodes)
    ll.remove(9)
    print()
    ll.print_linked_list()
    print()
    print("size of the linked list after removal", ll.numOfNodes)
