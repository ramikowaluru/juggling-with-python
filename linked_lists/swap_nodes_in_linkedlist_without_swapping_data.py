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
            s+=str(current_node.data)+"->"
            current_node = current_node.next

        print(s)

    def swapnode_withot_swapping_data(self, element1, element2):
        element1_prev = None
        element2_prev = None

        if element1==element2:
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.data==element1:
                element1_prev = current_node

            if current_node.next.data == element2:
                element2_prev = current_node.next

            current_node = current_node.next

        if element1_prev and element2_prev:
            temp = element1_prev.next
            element1_prev.next = element2_prev.next
            element2_prev.next = temp
            temp = element1_prev.next.next
            element1_prev.next.next=element2_prev.next.next
            element2_prev.next.next= temp




if __name__ == '__main__':
    ll = LinkedList()
    for i in [1,2,3,56,677,32,23]:
        ll.insert_a_node(i)
    ll.traverse()
    ll.swapnode_withot_swapping_data(677,23)
    ll.traverse()