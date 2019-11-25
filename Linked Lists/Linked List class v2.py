class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
    
    def length(self):
        current = self.head
        count = 0
        while current.next != None:
            current = current.next
            count +=1
        return count
    
    def display(self):
        elements = []
        current = self.head
        while current.next!=None:
            current = current.next
            elements.append(current.data)
        print(elements)
    
    def get(self,index):
        if index >= self.length():
            print("ERROR: Get index out of range")
            return None
        current_index = 0
        current = self.head
        while True:
            current = current.next
            if current_index == index: return current.data
            current_index +=1
      
    def erase(self,index):
        if index >= self.length():
            print("ERROR: Erase index out of range")
            return None
        current_index=0
        current = self.head
        while True:
            last_node = current
            current = current.next
            if current_index==index:
                last_node.next= current.next
                return 
            current_index +=1
            
            
my_list = linked_list()
my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

print(my_list.get(2))
my_list.erase(1)
my_list.display()
