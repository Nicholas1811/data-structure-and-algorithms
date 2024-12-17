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
            new_node.next = self.head  #Setting the next value of the new node to the self.head
            self.head = new_node #Setting the head value as the new node.


    #Adding at the back is slightly more complicated
    #Firstly, can copy the steps, if head is none, it can just set.
    #If the head is occupied, we will have to tranverse the LinkedList.

    def add_new_back(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            #While there is current.next value, what it does is it transverse the entire LinkedList
            #Until it reaches the last node, in which it will just set the current.next value to the new node.
            while current.next:
                current = current.next
                #at the last one, it adds a new node.
            current.next = new_node
            new_node.next = None
    
    #Adding by specific key is similar as well.
    #at specific index
    def add_by_key(self,data,key):
        new_node = Node(data)
        count = 0
        current = self.head
        while current.next:
            count += 1
            if count == key:
                new_node.next = current.next        
                current.next = new_node
            current = current.next

    def delete_front(self):
        current = self.head
        self.head = current.next

    def delete_back(self):
        current = self.head
        while current.next:
            current = current.next
            if current.next.next == None:
                current.next = None
                break
    
    def delete_at_key(self,key):
        count = 0
        previous_key = key-1
        current = self.head
        while current:
            if count == previous_key:
                current.next = current.next.next
            current = current.next
            count += 1
    def print_linked_list(self):
        current = self.head #Setting of self.head to current variable. self.head should be the first element of the LinkedList.
        while current: #While the variable current is not empty, it will print the current.data first and then, sets the current value to current.next
            print(current.data, end=" -> ")
            current = current.next
        

new_ll = LinkedList()
new_ll.add_new_front(2)
new_ll.add_new_front(3)
new_ll.add_new_front(4)
new_ll.add_by_key(5,1)
new_ll.add_new_back(6)
new_ll.add_new_back(7)
new_ll.add_new_back(8)
new_ll.delete_front()
new_ll.delete_back()
new_ll.delete_at_key(2)
new_ll.print_linked_list()