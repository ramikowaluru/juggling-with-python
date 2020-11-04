class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.frequency = 0

    def insert_a_node_at_the_beginning(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node


    def traverse(self):
        s = ""
        curr = self.head
        while curr:
            s +=str(curr.data)+"->"
            curr = curr.next

        print(s)

    def get_frequency_of_an_element(self, element):
        curr = self.head
        frequency = 0
        while curr:
            if curr.data == element:
                frequency +=1
            curr = curr.next

        return frequency

    def get_freq_using_recursion(self, current_node, element):
        if not current_node:
            return self.frequency
        if current_node.data == element:
            self.frequency +=1
        return self.get_freq_using_recursion(current_node.next, element)



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_a_node_at_the_beginning(1)
    ll.insert_a_node_at_the_beginning(23)
    ll.insert_a_node_at_the_beginning(23)
    ll.insert_a_node_at_the_beginning(4)
    ll.insert_a_node_at_the_beginning(45)
    ll.insert_a_node_at_the_beginning(23)
    print(ll.get_frequency_of_an_element(23))
    print(ll.get_freq_using_recursion(ll.head, 23))
