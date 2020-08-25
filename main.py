# Create a list
some_list = [1, 2, 3, 4, 5]

# Show the list and the id()
print(some_list)
print(id(some_list))

# Modify the list
some_list[1] = 'hot dog'
some_list[2] = ['dog', 'cat', None]

# Verify that the list has changed but the id() has not
print(some_list)
print(id(some_list))


"""Keep in mind that even two different list type objects that contain the same values will each have a unique result from id()."""

# Create two identical lists
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

# Show the id()s of list1
print(list1)
print(id(list1))

# Show the id()s of list2
print(list2)
print(id(list2))