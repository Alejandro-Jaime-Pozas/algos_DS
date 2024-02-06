class MyClass:
    shared_attribute = 0

obj1 = MyClass()
obj2 = MyClass()

obj1.shared_attribute = 30

print(obj1.shared_attribute)  # Output: 42
print(obj2.shared_attribute)  # Output: 42
