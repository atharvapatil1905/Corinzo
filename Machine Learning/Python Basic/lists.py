# List Methods
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Adds 6 to the end
my_list.insert(2, 10)  # Inserts 10 at index 2
my_list.remove(3)  # Removes first occurrence of 3
popped_value = my_list.pop()  # Removes and returns the last element
my_list.reverse()  # Reverses the list
my_list.sort()  # Sorts the list

print("List after operations:", my_list)


for i in my_list:
    print(i)
