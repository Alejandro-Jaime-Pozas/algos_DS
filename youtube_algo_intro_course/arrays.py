# ARRAYS DATA STRUCTURES BUILT INTO PYTHON
# GOOD FOR ACCESSING DATA
# BAD AT INSERTING AND DELETING SINCE LINEAR TIME O(n)

new_list = [1, 2, 3] # list values in python are NOT stored in memory, instead the references to each value are stored in memory and then retrieve their respective values from elsewhere. this is why accessing a list's values is CONSTANT TIME O(1)...

# result = new_list[100] # this returns an error bc a list is a contiguous set of data in memory, so when there is no matching index the index error is returned
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break 

new_list.insert(0, 4) # this is linear time since worst case you need to insert an object into the first index, so every other object needs to move one index to the right, which takes linear time to do in python.
new_list.append(5) # this is constant time O(1) since obj is added to end of list, no need to change anything else; but behind the scenes its more complex
new_list.extend([10,20,30]) # O(k) where k represents number of objects being added to existing list
new_list.remove(10) # linear runtime O(n) since needs to change other indeces
print(new_list)

list