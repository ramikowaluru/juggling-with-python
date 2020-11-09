class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_a_node_at_head(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def traverse(self):
        s = ""
        curtrent_node = self.head
        while curtrent_node:
            s += str(curtrent_node.data)+"->"
            curtrent_node = curtrent_node.next

        print(s)


    def get_the_doubly_refrenced_node(self):
        fast_ref = self.head
        slow_ref = self.head

        while fast_ref:
            fast_ref = fast_ref.next
            slow_ref = slow_ref.next.next
            if slow_ref==fast_ref:
                print("There is a loop")
                return slow_ref

    def get_the_legth_of_the_loop(self):
        doubly_referenced = self.get_the_doubly_refrenced_node()
        loop_length=0
        temp = doubly_referenced
        while temp:
            if temp.next==doubly_referenced:
                break
            loop_length +=1
            temp = temp.next

        return loop_length

if __name__ == '__main__':

    ll = LinkedList()
    lelements = [1, 2,"er",34,"sdaf",345]


    for i in lelements:
        ll.insert_a_node_at_head(i)

    ll.traverse()

    ll.head.next.next.next.next.next.next = ll.head.next.next

    print(ll.get_the_legth_of_the_loop())

