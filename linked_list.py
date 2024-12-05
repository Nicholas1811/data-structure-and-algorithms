#Class to create a node. Initialises the node
class Node:
    def __init__(self,data):
        #None because at the start it should not be reference. Should not be initialised as a compulsory one.
        self.data = data
        self.next = None
        
#Creation of the actual link list. Example from https://www.w3schools.com/dsa/dsa_data_linkedlists_types.php
node_1 = Node(10)
node_2 = Node(20)
node_3 = Node(30)
node_4 = Node(40)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

currentNode = node_1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next



#Class to create the actual linked list
# class LinkedList:
#     def insert(self,data):
#         #Creates a new node for the data.
#         new_data = Node(data)
#         #If there is nothing in the head of the LinkedList, it will set the data node as the head.
#         if self.head is None:
#             self.head = new_data
#             return
#         else:
#         #If there is something in the head of the LinkedList, meaning a node,  
#             new_data.next = self.head
#             self.head = new_data

