search_names = ['a','b','c','d','e','f']
names = ['e','v','c','b','a','f','z','m']

def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None 

# Big O(n^2 since looping through 2 lists one nested in the other)
if __name__=="__main__":
    for n in search_names:
        index = index_of_item(names, n)
        print(n, 'at index:', index)