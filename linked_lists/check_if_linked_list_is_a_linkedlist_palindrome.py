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
        s = ""
        current_node = self.head

        while current_node:
            s = str(current_node.data)+"->"
            current_node = current_node.next

        print(s)


    def cehck_if_the_linked_list_is_palin_drom(self):
        """
        Idea is using a list to strore the elements of the linked list by traversing the linked list
        and then we start travese again and compare the elements of the list we stored
        :return:
        """
        ll_elements = []

        current_node = self.head
        while current_node:
            ll_elements.append(current_node.data)
            current_node = current_node.next

        # reassing current node with head
        current_node = self.head

        while current_node:
            if current_node.data != ll_elements.pop():

                return "Not a palindrome"
            current_node = current_node.next

        return "Linked list is a palindrome"


if __name__ == '__main__':
    # linked list which is a palindrom
    ll = LinkedList()
    l = [1,2,3,2,1]
    for i in l:
        ll.insert_at_head(i)
    print(ll.cehck_if_the_linked_list_is_palin_drom())

    # linked list which is not a palindrome
    ll2 = LinkedList()
    l2 = [2,3,4,5]
    for i in l2:
        ll2.insert_at_head(i)
    print(ll2.cehck_if_the_linked_list_is_palin_drom())