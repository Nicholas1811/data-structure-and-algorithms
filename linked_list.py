#Class to create a node. Initialises the node
class Node:
    def __init__(self,data):
        #None because at the start it should not be reference. Should not be initialised as a compulsory one.
        self.data = data
        self.next = None
        
#Creating of linked list with a LinkedList Class
class LinkedList:
    #When linked list is initialised, the head is none.
    #Adding can be done in 3 ways. Add at the front, middle, or back

    def __init__ (self):
        self.head = None
    
    #Adding at the front involves 3 steps
    #Firstly, get the new data and set it to the node class so it should have (Data, Node)
    #Secondly, check if head exists. If head does not exists, set the head as the new_data
    #If the head exists, set new_data reference to the head and then, set the new_data as the head.
    def add_new_front(self,data):
        new_node = Node(data) # From value 20 becomes (20,next value)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head  #Setting the next value to the second value
            self.head = new_node


    #Adding at the back is slightly more complicated
    #Firstly, can copy the steps, if head is none, it can just set.
    #If the head is occupied, we will have to tranverse the LinkedList.

    def add_new_back(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    #Adding by specific key is similar as well.
    #Takes in the value, and we can add a counter

    def add_by_key(self,data,key):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            count = 1 #Tracking of index
            while current:
                current = current.next
                count+=1
                if count == key:

    def print_linked_list(self):
        current = self.head #Setting of self.head to current variable. self.head should be the first element of the LinkedList.
        while current: #While the variable current is not empty, it will print the current.data first and then, sets the current value to current.next
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        

new_ll = LinkedList()
new_ll.add_new_front(10)
new_ll.add_new_front(20)
new_ll.add_new_front(30)
new_ll.add_new_back(100)
new_ll.print_linked_list()