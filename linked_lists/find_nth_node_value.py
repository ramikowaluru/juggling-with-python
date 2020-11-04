class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_an_element_into_the_linked_list(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node


    def get_nth_node_value(self, position):
        current_node = self.head
        while position>1 and current_node:
            position-=1
            current_node = current_node.next
        if current_node:
            return current_node.data
        else:
            print("element is not in the list")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_an_element_into_the_linked_list(1)
    ll.insert_an_element_into_the_linked_list(2)
    ll.insert_an_element_into_the_linked_list(63)
    ll.insert_an_element_into_the_linked_list(4)
    ll.insert_an_element_into_the_linked_list(5)
    print(ll.get_nth_node_value(5))