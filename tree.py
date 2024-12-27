#Binary search tree implementation

class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        data_insert = Node(data)

        if self.root is None:
            self.root = data_insert
        
        #Setting it to a variable to while loop over
        current = self.root

        while current:
            #If the root node is lower, it goes to the left
            if data < current.data:
                #the check here is to check that the current left is empty. if empty, it creates
                if current.left is None:
                    current.left = data_insert
                    return
                current = current.left
            #If the data is higher, it goes to the right
            elif data > current.data:
                if current.right is None:
                    current.right = data_insert
                    return
                current = current.right
            else:
                print(f"{data} already exist.")
                return
        
    def search(self,search):
        current = self.root
        while current:
            if search < current.data:
                current = current.left
            elif search > current.data:
                current = current.right
            elif search == current.data:
                break
        print(f"{current.data} is found!")   
    def delete(self,del_key):
        current = self.root
        parent = None
        while current and current.data != del_key:
            parent = current
            if del_key < current.data:
                current = current.left
            elif del_key > current.data:
                current = current.right
        
        #Delete the leaf node (80)
        if current.left is None and current.right is None:
            if current.data > parent.data:
                parent.right = None
            else:
                parent.left = None
        
        #Delete the parent node (One child) - Child gets replaced.
    def delete_middle(self,del_key):
        current = self.root
        parent = None
        while current and current.data != del_key:
            parent = current
            if del_key < current.data:
                current = current.left
            elif del_key > current.data:
                current = current.right
        
        #Delete the parent node (One child) - Child gets replaced.
        if current.left or current.right:
            current = parent
            parent = current
            parent.left == None
            parent.right == None

    #Delete for nodes with two children.
    #2 ways to do so: Replace with the predecessor or successor.
    #If node is = 80, 70 can be used or 90.


    def delete_top(self,del_key):
        current = self.root
        parent = None
        while current and current.data != del_key:
            parent = current
            if del_key < current.data:
                current = current.left
            elif del_key > current.data:
                current = current.right
        #if current.left and current.right:

    
    def inorder(self,root = None):
        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                
        

            






bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
bst.search(50)
bst.delete(80)
bst.delete(70) #Deleting single child.
bst.inorder()




            
        