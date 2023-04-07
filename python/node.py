class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) == int:
            self.__data = data
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        # print(type(Node(1)))
        # print("class name: ", self.__class__)
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if type(next_node) == self.__class__ or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def insert_at_end(self, value):
        node = Node(data=value)
        if not self.__head:
            # print("New sll created")
            self.__head = node
        else:
            curr = self.__head
            while curr.next_node is not None:
                curr = curr.next_node

            curr.next_node = node


    def print_list(self):
        if self.__head is None:
            print("No head")
        else:
            print(self.__head.data, end=", ")
            current_node = self.__head.next_node
            # print(self.__head.next_node.data)
            while current_node:
                if not current_node.next_node:
                    break
                else:
                    print(current_node.next_node.data, end=", ")
                current_node = current_node.next_node

        

    
