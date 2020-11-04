class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_a_node_in_linked_list(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def find_an_lem_element_in_the_linkled_list(self, element):
        current_node = self.head
        while current_node:
            if current_node.data == element:
                return "element is found"
            current_node = current_node.next

        return "element is not found"


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_a_node_in_linked_list(1)
    ll.insert_a_node_in_linked_list(4)
    ll.insert_a_node_in_linked_list(7)
    print(ll.find_an_lem_element_in_the_linkled_list(4))
    print(ll.find_an_lem_element_in_the_linkled_list(13))