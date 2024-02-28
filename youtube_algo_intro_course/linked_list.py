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
        # if node is attached to linked list, could save time complexity for size() function maybe by auto-adding the count of list elements + 1 if there's a new node attached to link list, and also add when removing node or inserting node

    def __repr__(self):
        return f"<Node| data: {self.data}>"
    

class LinkedList:
    '''
    Singly linked list
    '''

    def __init__(self):
        # better naming convention would be self.head_node, since it's a node or None if last node
        self.head = None 

    def is_empty(self):
        return not self.head
    
    def size(self):
        '''
        Returns the number of nodes in the list
        works as long as nodes are linked, ie nodes have a next_node property until this finds the last tail node with no next_node
        O(n) time
        '''
        current = self.head # this to not modify the current list's actual self.head
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
        # first need to set current self.head old node to new node's next node, so there will be 2 self.heads, and then update the current self.head to point to the new node
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

        # if index is positive
        if index > 0:
            new = Node(data)

            # store index and self.head to not modify their original values
            position = index 
            current = self.head 

            # while index > 1, move along the nodes in linked list until 1 is reached, which means that's the index to insert new node into
            while position > 1:
                current = current.next_node
                position -= 1

            # set the traversed list's current node's next node to the new node, and the new node's next node to current's next node to sever the ties between current node's original next node
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
            # if node is also the list's head, set list's head node to current's next node
            if current.data == key and current is self.head:
                found = True 
                self.head = current.next_node 
            elif current.data == key:
                found = True 
                # sever the tie between the current node and next node by linking the prev node to current's next node
                previous.next_node = current.next_node
            else:
                # set current node to previous, and next node to current for next iteration in while loop
                previous = current 
                current = current.next_node
        return current # return the removed node

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head 
            position = 0

            # traverse the list until position is no longer less than index (which means its equal to index)
            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        # need to traverse list and somehow make it visually understandable
        nodes = []
        current = self.head 

        while current:
            if current is self.head: # if this node is the first/newest node
                nodes.append(f"[Head: {current}]")
            elif current.next_node is None: # if this node is the last/oldest node
                nodes.append(f"[Tail: {current}]")
            else:
                nodes.append(f"[{current}]")

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