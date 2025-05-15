# Set Methods
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adds 6 to the set
my_set.remove(3)  # Removes 3 from the set
my_set.discard(10)  # Discards 10 if present (no error if absent)
new_set = {4, 5, 6, 7}
union_set = my_set.union(new_set)  # Combines both sets
intersection_set = my_set.intersection(new_set)  # Finds common elements


for i in my_set:
    print(i)
