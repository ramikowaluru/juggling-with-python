class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes =0

    def insert_node(self, data):
        node = Node(data)
        self.num_of_nodes += 1
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def deleting_nth_node(self, n):
        if self.head and n<=self.num_of_nodes and n>0:
            curret_node = self.head
            prev_node = None
            while n>1:
                n -= 1
                prev_node=curret_node
                curret_node = curret_node.next
            self.num_of_nodes -= 1
            if prev_node:
                prev_node.next = curret_node.next
                del curret_node
            else:
                curret_node = self.head
                self.head = self.head.next
                del curret_node
        else:
            print("linked list is empty, there is nothing to delete")

    def travesal(self):
        s=""
        current_node = self.head
        while current_node:
            s+=str(current_node.data)+"->"
            current_node = current_node.next
        print("element of the linked list are",s)


if __name__ == '__main__':
    # ll stands for linked list
    ll = LinkedList()
    ll.insert_node(1)
    ll.insert_node(2)
    ll.insert_node(10)
    ll.insert_node(12)
    ll.travesal()
    # removing the head node
    ll.deleting_nth_node(1)
    # linked list after removing the head node
    ll.travesal()
    print("linkedlist before deleting the 2th node")
    ll.travesal()
    ll.deleting_nth_node(2)
    print("linkedlist after deleting the 2th node")
    ll.travesal()



