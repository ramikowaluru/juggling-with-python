class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None


    def get_insert_a_node(self, data):

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
            s += str(current_node.data)+"->"
            current_node = current_node.next

        print(s)

    def deleting_redundant_elements_using_two_references(self):
        ref1 = self.head
        ref2= self.head

        while ref1 and ref1.next:
            ref2 = ref1
            print("hi")
            self.traverse()
            while ref2.next:
                if ref1.data==ref2.next.data:
                    temp = ref2.next
                    ref2.next = ref2.next.next
                    del temp
                else:
                    ref2 = ref2.next

            ref1 = ref1.next



if __name__ == '__main__':
    ll = LinkedList()
    l = [1,2,3,2,1,2,3,4]
    for i in l:
        ll.get_insert_a_node(i)

    ll.traverse()
    ll.deleting_redundant_elements_using_two_references()
    ll.traverse()