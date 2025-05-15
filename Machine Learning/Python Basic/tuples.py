my_tup = (1, 2, 3, 4, "Hello", 6, 2, 2, 2, 7)

print(my_tup)


# Tuple Methods (Tuples are immutable, so methods are limited)
my_tuple = (1, 2, 3, 4, 2, 5, 2)
count_2 = my_tuple.count(2)  # Counts occurrences of 2
index_3 = my_tuple.index(3)  # Finds index of first occurrence of 3

print("Tuple count of 2:", count_2)
print("Tuple index of 3:", index_3)


# Looping through a tuple
for i in my_tup:
    print(i)
