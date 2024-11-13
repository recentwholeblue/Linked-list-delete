#Create node class
class Node:
    #Make node
    def __init__(self, data):
        self.data = data
        self.next = None

#Create Linked List class
class LinkedList:
    #Make head
    def __init__(self):
        self.head = None  #Create head

    #Inserts new node
    def insert(self, data):
        node = Node(data)  #Create node
        node.next = self.head  #Attach head to node
        self.head = node

    #Display linked list
    def display(self):
        current = self.head
        #Show each node while going through each node
        while current: 
            print(current.data, end=" -> ")  
            current = current.next
        print("None") #Show the end of list

    #Function to delete head
    def delete(self):
        #Check if list is empty
        if self.head is None:
            return None  #If empty, returns None
        
        data = self.head.data
        self.head = self.head.next
        return data

ll = LinkedList()
ll.insert(10)  
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete()
ll.display()
