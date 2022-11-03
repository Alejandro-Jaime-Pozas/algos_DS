class Node:
    '''
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    '''

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node| data: {self.data}>"


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self,):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the num of nodes in the list
        Takes O(n) time bc it traverses all nodes
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        '''
        Adds a new node containing data at head of the list
        Takes O(1) time
        '''
        new_node = Node(data)
        new_node.next_node = self.head # refers to the next node at start of list (which is always None since you're setting this node to the first node in the list)
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing the data that matches the key
        Return the node or None if not found
        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        '''
        Return a string represenatation of the list
        Takes O(n) time
        '''

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node
        return '-> '.join(nodes)