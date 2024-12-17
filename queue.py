# type: ignore
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
    def enqueue(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.next = None
    def dequeue(self):
        current = self.head
        self.head = current.next
    def show(self):
        current = self.head
        while current:
            print(current.data, end= "->")
            current = current.next




new_llq = LinkedListQueue()
new_llq.enqueue(1)
new_llq.enqueue(2)
new_llq.enqueue(3)
new_llq.enqueue(4)
new_llq.enqueue(5)
new_llq.dequeue()
new_llq.show()


class QueueArray:
    def __init__ (self):
        self.queue = []
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        self.queue.pop(0)
    def show(self):
        for i in self.queue:
            print(i)

new_qa = QueueArray()
new_qa.enqueue(1)
new_qa.enqueue(2)
new_qa.enqueue(3)
new_qa.dequeue()
new_qa.show()