class Node:
    def __init__(self, data):
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_a_node_at_head(self, data):
        node = Node(data)

        node.next = self.head
        self.head = node

    def traverse(self):
        current_node = self.head
        s = ""
        while current_node:
            s += str(current_node.data)+"->"
            current_node = current_node.next
        print(s)

    def get_end(self, current_node):

        while current_node and current_node.next:
            current_node = current_node.next

        return current_node

    def partition(self,start,end, new_start, new_end):
        pivot = end
        prev = None
        current_node = start
        last_node = pivot

        while current_node!=pivot:
            if current_node.data < pivot.data:
                if new_start is None:
                    new_start = current_node
                prev = current_node
                current_node = current_node.next
            else:
                if prev:
                    prev.next = current_node.next
                temp = current_node.next
                current_node.next = None
                last_node.next = current_node
                last_node = current_node
                current_node = temp
        if new_start is None:
            new_start= pivot
        return pivot, new_start, new_end


    def quick_sort(self, start, end):
        # checking where we reached end or there is only one emelent for the given start and end
        if not start or start==end:
            return start
        new_start = None
        new_end = None

        pivot, new_start, new_end = self.partition(start, end, new_start, new_end)

        if new_start != pivot:
            temp = new_start
            if temp:
                while temp.next!=pivot:
                    temp = temp.next
                temp.next = None

            new_start = self.quick_sort(new_start, temp)
            temp = self.get_end(new_start)
        temp.next = pivot

        return new_start


if __name__ == '__main__':
    ll = LinkedList()
    for i in [12, 69654, 12, 32, 2, 16, 1, 6]:
        ll.insert_a_node_at_head(i)
    ll.traverse()
    ll.head = ll.quick_sort(ll.head, ll.get_end(ll.head))

    ll.traverse()