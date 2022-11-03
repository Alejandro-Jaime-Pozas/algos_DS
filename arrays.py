new_list = [1,2,3]
result = new_list[1]

if 1 in new_list:
    print(True)

for n in new_list:
    if n ==1:
        print(True)

# arr.insert() is O(n) since each value needs to be moved an index
# arr.append() is O(1) since its added to the end of array
# arr.delete() is O(n) since needs to move all the indexes over

# append is O(1) bc of how python interprets it