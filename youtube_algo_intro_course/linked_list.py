# LINKED LISTS ARE MADE UP OF NODES WHICH ARE SELF REFERENTIAL OBJECTS
# SINGLY LINKED LIST: EACH NODE STORES A REF TO THE NEXT NODE IN THE LIST
# DOUBLY LINKED LIST: EACH NODE STORES REF TO PREV AND NEXT NODE IN THE LIST

class Node:
    '''
    An obj for storing a single node of a linked list.
    models 2 attributes - data and the link to the next node in the list
    '''
    data = None 
    next_node = None 

    def __init__(self, data):
        self.data = data 

    def __repr__(self):
        return f"<Node| data: {self.data}"
    

class LinkedList:
    '''
    Singly linked list
    '''

    def __init__(self):
        self.head = None 

    def is_empty(self):
        return not self.head
    
    def size(self):
        '''
        Returns the number of nodes in the list
        works as long as nodes are linked, ie nodes have a next_node property until this finds the last tail node with no next_node
        O(n) time
        '''
        current = self.head 
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count 
    
    def add(self, data):
        '''
        Create a new Node instance, assign current list head node as the next node for the new Node instance created, set the new list head node to new Node instance created
        O(1) time
        '''
        new_node = Node(data)
        new_node.next_node = self.head 
        self.head = new_node