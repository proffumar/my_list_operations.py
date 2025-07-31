
# My list Operations Assignment for assignment 2

# Step 1: Create an empty list
my_list = []

# Step 2: Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)

# Step 3: Insert 15 at the second position (index 1), but the indexing start from 0
my_list.insert(1, 15) # inserting 15 at position 2 on the list

# Step 4: Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of value 30
index_of_30 = my_list.index(30)

# Final Outputs
print("Final list:", my_list)
print("Index of 30:", index_of_30)
