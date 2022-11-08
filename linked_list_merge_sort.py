from linked_list import LinkedList

# l = LinkedList()
# l.add(1)
# print(l)

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - recursively divide the linked list into sublists conatining a single node
    - repeatedly merge the sublists ro produce sorted sublists until one remains

    returns a sorted linked list
    """

    if linked_list.size() == 1 or linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)