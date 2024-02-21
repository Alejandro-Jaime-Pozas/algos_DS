# LINKED LISTS ARE MADE UP OF NODES WHICH ARE SELF REFERENTIAL OBJECTS
# SINGLY LINKED LIST: EACH NODE STORES A REF TO THE NEXT NODE IN THE LIST
# DOUBLY LINKED LIST: EACH NODE STORES REF TO PREV AND NEXT NODE IN THE LIST
# CHECK THIS IN PYTHON TUTOR SITE HOW IT WORKS

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

    def search(self, key):
        '''
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        O(n) time
        '''
        
        current = self.head 

        while current:
            if current.data == key:
                return current 
            else:
                current = current.next_node
        return None 

    def insert(self, data, index):
        '''
        Insert a new node containing data at index position
        Insertion takes O(1) time but finding the node at the insertion point takes O(n) time

        O(n) time
        '''
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index 
            current = self.head 

            while position > 1:
                current = current.next_node
                position -= 1

            current.next_node = new
            new.next_node = current.next_node 

    def remove(self, key):
        '''
        Removes node containing data that matches the key
        REturns the node or None if key doesn't exist
        O(n) time
        '''
        current = self.head 
        previous = None 
        found = False 

        while current and not found:
            if current.data == key and current is self.head:
                found = True 
                self.head = current.next_node 
            elif current.data == key:
                found = True 
                previous.next_node = current.next_node
            else:
                # set current node to previous, and next node to current for next iteration
                previous = current 
                current = current.next_node
        return current 

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head 
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        nodes = []
        current = self.head 

        while current:
            if current is self.head: # if this node is the first/newest node
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None: # if this node is the last/oldest node
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node
        return ' -> '.join(nodes)
    

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# l = LinkedList()
# l.add(n1)
# l.add(n2)
# l.add(n3)
# l
# l.insert(n3, 100)
# l
# l.remove(30)