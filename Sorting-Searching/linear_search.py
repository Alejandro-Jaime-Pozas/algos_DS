import names as n

names = [n.get_full_name() for _ in range(1000)]
search_names = [n.get_full_name() for _ in range(100)]

def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None

for person in search_names:
    index = index_of_item(names, person)
    print(index)