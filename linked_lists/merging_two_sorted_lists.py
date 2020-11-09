class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def traverse(self):
        s=""
        current_node = self.head
        while current_node:
            s += str(current_node.data)+"=>"
            current_node = current_node.next
        print(s)

    def merge_two_sorted_lists(self,ll1,ll2):
        temp2 = Node("dummy")
        temp = temp2
        ll1 = ll1
        ll2 = ll2
        while True:
            # if we reach end of the first linked list then assing rest of the second to temp and exit loop
            if ll1 is None:
                temp.next = ll2
                break
            # if we reach end of the second linked list then assign rest of the firt list to temp anbd exit while loop
            if ll2 is None:
                temp.next = ll1
                break

            if ll1.data<=ll2.data:
                temp.next = ll1
                ll1 = ll1.next
            else:
                temp.next = ll2
                ll2 = ll2.next

            temp = temp.next

        return temp2.next


if __name__ == '__main__':
    ll1 = LinkedList()
    for i in [10,9,8,7,6]:
        ll1.insert_at_head(i)
    ll2 = LinkedList()
    for i in [466,234,45,6]:
        ll2.insert_at_head(i)
    ll1.traverse()
    # ll2.traverse()
    ll1.head = ll1.merge_two_sorted_lists(ll1.head,ll2.head)
    ll1.traverse()