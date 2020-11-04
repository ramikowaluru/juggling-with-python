class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_a_node(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.num_of_nodes += 1
        else:
            node.next = self.head
            self.head = node
            self.num_of_nodes += 1

    def traverse(self):
        s=""
        current_node = self.head
        while current_node:
            s+=str(current_node.data)+"->"
            current_node = current_node.next
        print(s)

    def find_middle_element_by_using_mid_positon(self):
        mid = self.num_of_nodes//2
        current_node = self.head
        while mid>0:
            mid -= 1
            current_node = current_node.next

        return current_node.data
    def using_two_pointers(self):
        actual_ref = self.head
        secondary_ref = self.head
        while secondary_ref and secondary_ref.next:
            secondary_ref = secondary_ref.next.next
            actual_ref = actual_ref.next

        return actual_ref.data

    def find_mid_element_by_tracking_odd_positions(self):
        pos_counter = 1
        current_node = self.head
        mid =self.head

        while current_node:
            pos_counter += 1
            current_node = current_node.next
            if pos_counter%2==1:
                mid = mid.next

        return mid.data


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_a_node(2)
    ll.insert_a_node("df")
    ll.insert_a_node("asd")
    ll.insert_a_node(34)
    ll.insert_a_node("w")
    # ll.insert_a_node("sd")
    ll.traverse()
    print(ll.find_middle_element_by_using_mid_positon())
    print(ll.using_two_pointers())
    print(ll.find_mid_element_by_tracking_odd_positions())


