class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None


    def get_insert_a_node(self, data):

        node = Node(data)
        print(node.data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def traverse(self):
        s = ""
        current_node = self.head

        while current_node:
            s += str(current_node.data)+"->"
            current_node = current_node.next

        print(s)

    def remove_duplicates_from_sorted_linkedlist(self):
        """We will be going to use tow references
        first reference will move until it meets the break condition
        second reference will move to the next only if sees the different data in the first pointer than it is having.
        Before moving second reference we reassing it's next with the first reference and reassing
        it to the next of it's point that it the location of first reference
        """
        fast_node = self.head
        slow_node = self.head
        while fast_node.next:
            fast_node = fast_node.next
            if fast_node.data != slow_node.data:
                slow_node.next = fast_node
                slow_node = slow_node.next


if __name__ == '__main__':
    # linked list which is a palindrom
    ll = LinkedList()
    l = [1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    for i in l:
        ll.get_insert_a_node(i)
    ll.traverse()
    ll.remove_duplicates_from_sorted_linkedlist()
    ll.traverse()

