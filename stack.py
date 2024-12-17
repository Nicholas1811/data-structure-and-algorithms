#Class to create a node. Initialises the node
class Node:
    def __init__(self,data):
        #None because at the start it should not be reference. Should not be initialised as a compulsory one.
        self.data = data
        self.next = None
        
#Creating of linked list with a LinkedList Class
class StackedLinkedList:
    #When linked list is initialised, the head is none.
    #Adding can be done in 3 ways. Add at the front, middle, or back

    def __init__ (self):
        self.head = None
    
    def push(self,data):
        new_data = Node(data)
        if self.head == None:
            self.head = new_data
            return
        else:
            new_data.next = self.head
            self.head = new_data
    def pop(self):
        current = self.head
        self.head = current.next
    def show(self):
        current = self.head
        while current:
            print(current.data, end="-> ")
            current = current.next

        

new_ll = StackedLinkedList()
new_ll.push(10)
new_ll.push(3)
new_ll.push(11)
new_ll.push(12)
new_ll.push(13)
new_ll.pop()
new_ll.pop()

new_ll.show()

class StackArray:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            self.stack.pop()
    def show(self):
        for i in self.stack:
            print(i)


new_arr = StackArray()
new_arr.push(1)
new_arr.push(2)
new_arr.push(3)
new_arr.pop()
new_arr.show()
