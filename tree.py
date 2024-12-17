#Binary search tree implementation

class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            data_node = self.root
            while data_node:
                if data < data_node.data:
                    data_node.left == data
                    data_node = data_node.left
                elif data > data_node.data:
                    data_node.right == data
                    data_node = data_node.left


    
    def show(self):
        print(self.root.data)
        print(self.root.left)
        print(self.root.right)



new_bst = BinarySearchTree()
new_bst.insert(10)
new_bst.insert(5)
new_bst.insert(15)
new_bst.show()




            
        