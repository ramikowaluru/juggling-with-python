class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_into_the_linked_list(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def traversal(self):
        s=""
        current_node = self.head
        while current_node:
            s+=str(current_node.data)+"->"
            current_node = current_node.next
        print(s)

    def fining_nth_node_from_end_with_out_using_the_length_of_linked_list(self, position_from_end):
        traverse_ref = self.head
        actual_ref = self.head
        position = 0
        while position<position_from_end:
            position+=1
            traverse_ref = traverse_ref.next

        while traverse_ref:
            traverse_ref = traverse_ref.next
            actual_ref = actual_ref.next
        return actual_ref.data

    def finding_nth_element_from_end(self,position_from_end):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next

        current_node = self.head
        position_from_start = length - position_from_end
        while position_from_start>0:
            position_from_start -=1
            current_node = current_node.next
        return current_node.data


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_node_into_the_linked_list(23)
    ll.insert_node_into_the_linked_list(25)
    ll.insert_node_into_the_linked_list(32)
    ll.insert_node_into_the_linked_list(2)
    ll.insert_node_into_the_linked_list(3)
    print(ll.traversal())
    print("3rd element from the end is ", ll.fining_nth_node_from_end_with_out_using_the_length_of_linked_list(1))
    print("3rd element from the end is ", ll.finding_nth_element_from_end(1))
