from quicksort import quicksort
import os

# start with the exact same code as quicksort.py file
sorted_names = quicksort(['e','v','c','b','a','f','z','m'])

for n in sorted_names:
    print(n)

# if True:
#     os.mkdir(os.path.join(os.path.dirname(__file__), 'new_directory'))