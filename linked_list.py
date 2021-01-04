class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        super(Node, self).__init__()


class LinkedList(object):
    def __init__(self, circular=False):
        self.head = None
        self.tail = None
        self.circular = circular
        super(LinkedList, self).__init__()

    def push_head(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

        # For first Node set both head and tail
        if not self.tail:
            self.tail = self.head

        # Circular linked list
        if self.circular:
            self.tail.next = self.head
        return None

    def push_tail(self, item):
        new_node = Node(item)
        self.tail.next = new_node
        self.tail = new_node

        # For first Node set both head and tail
        if not self.head:
            self.head = self.tail

        # Circular linked list
        if self.circular:
            self.tail.next = self.head
        return None

    def print_ll(self):
        print("The data is: ")
        temp = self.head

        if temp:
            if self.circular:
                while True:
                    print(temp.data, end="->")
                    temp = temp.next
                    if temp == self.head:
                        break
                print()
            else:
                while temp:
                    print(temp.data, end='->')
                    temp = temp.next
                print()

    def split(self):
        center = self.head
        head = self.head
        index = 1
        while True:
            if index % 2 == 0:
                center = center.next
            head = head.next
            index += 1
            if head.next is None:
                break
        headB = center.next
        center.next = None
        return headB

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def delete_key(self, x, first_occ=True):
        temp = self.head
        # Delete head node
        if temp.data == x:
            next_node = temp.next
            self.head = next_node

            if self.circular:
                self.tail.next = self.head

            if first_occ:
                return None
            else:
                self.delete_key(x)
        else:
            prev_node = temp
            temp = temp.next

            if self.circular:
                # Check the remaining Node
                while True:
                    if temp.data == x:
                        next_node = temp.next
                        prev_node.next = next_node

                        # If the deleted node is the last node
                        if temp == self.tail:
                            self.tail = prev_node
                            self.tail.next = self.head

                        # If delete only the first occurrence
                        if first_occ:
                            break
                        prev_node = next_node
                    else:
                        prev_node = temp
                    temp = temp.next

                    if temp == self.head:
                        break
            else:
                # Check the remaining Node
                while temp:
                    if temp.data == x:
                        next_node = temp.next
                        prev_node.next = next_node

                        # If delete only the first occurrence
                        if first_occ:
                            break
                    else:
                        prev_node = temp
                    temp = temp.next


linked_list = LinkedList(circular=False)
linked_list.print_ll()
linked_list.push_head(1)
linked_list.push_head(2)
linked_list.push_head(3)
linked_list.push_head(4)

linked_list.push_tail(5)
linked_list.push_tail(6)
linked_list.push_tail(7)
# linked_list.push_tail(8)

# linked_list.print_ll()
# print('after deletion:', 3)
# linked_list.delete_key(3)
# linked_list.print_ll()
# print('after deletion:', 4)
# linked_list.delete_key(4)
# linked_list.print_ll()
# print('after deletion:', 7)
# linked_list.delete_key(7)
# linked_list.print_ll()
# print('after adding:', 7)
# linked_list.push_tail(7)
# linked_list.print_ll()
# print('after adding:', 7)
# linked_list.push_head(7)
# linked_list.print_ll()
head = linked_list.split()

prev = None
current = head
while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
head = prev
while head:
    print(head.data, end="->")
    head = head.next
print()

linked_list.print_ll()
linked_list.reverse()
linked_list.print_ll()
