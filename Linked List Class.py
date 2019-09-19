class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next_node = next

    def get_next(self):
        return self.next_node

    def set_next(self, next):
        self.next_node = next

    def get_data(self):

        return self.data

    def set_data(self,data):
        self.data = data


class LinkedList(object):
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        current_node = self.root
        prev_node = None
        while current_node:
            if current_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.root = current_node
                self.size -= 1
                return True        # found data
            else:
                prev_node = current_node
                current_node = current_node.get_next()
        return False               # did not find data

    def find(self, data):
        current_node = self.root
        while current_node:
            if current_node.get_data() == data:
                return data
            else:
                current_node = current_node.get_next()

        return None


myLinkedList = LinkedList()
myLinkedList.add(12)
myLinkedList.add(10)
myLinkedList.add(5)
print(myLinkedList.remove(10))
print(myLinkedList.get_size())


