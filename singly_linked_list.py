class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_LinkedList(self):
        return_array = []
        if self.head == None:
            print("Empty Linked List")
        else:
            node = self.head
            while node is not None:
                return_array.append(f'{node.value} =>')
                node = node.nextnode

        # print(return_array, "Length:", self.length)
        return {
            'linked_list': return_array,
            'length': self.length,
            'head': self.head.value,
            'tail': self.tail.value
        }

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nextnode = new_node
            self.tail = new_node
        self.length = self.length + 1

    def pop(self):
        if self.length == 0:
            print(None)

        newHead = self.head
        current = newHead

        while current.nextnode:
            newHead = current
            current = current.nextnode

        self.tail = newHead
        newHead.nextnode = None
        self.length = self.length - 1

        if self.length == 0:
            self.head = None
            self.head = None

    def unshift(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nextnode = self.head
            self.head = new_node

        self.length = self.length + 1

    def shift(self):
        if self.length == 0:
            return(None)
        else:
            self.head = self.head.nextnode

        self.length = self.length - 1

    def get_index(self, index):
        if index < 0 or index > self.length - 1:
            return "Index Out Of Range"
        current = self.head
        counter = 0

        while counter != index:
            current = current.nextnode
            counter += 1

        return current

    def set_index(self, index, value):
        if index < 0 or index > self.length - 1:
            return "Index Out Of Range"

        node = self.get_index(index)
        node.value = value

        return node


linked_list = SinglyLinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)
linked_list.push(5)
# linked_list.pop()
linked_list.shift()
linked_list.unshift(0)
linked_list.unshift(-9)
linked_list.set_index(4, "HII")

print(linked_list.print_LinkedList())
# print(linked_list.get_index(0).value)
