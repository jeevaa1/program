# Initializing the rank list with sample data
rank_list = {
    '123': 90,
    '456': 85,
    '789': 92,
    '101': 80,
    '202': 95
}
print("Rank List:")
print(rank_list)

# Check whether the given register number is available in the list
reg_no = input("Enter register number to check availability: ")
if reg_no in rank_list:
    print(f"Register number {reg_no} is available in the list.")
else:
    print(f"Register number {reg_no} is not available in the list.")

# Modify a mark
reg_no = input("Enter register number to modify mark: ")
new_mark = int(input("Enter new mark: "))
rank_list[reg_no] = new_mark
print("Rank List after modifying mark:")
print(rank_list)

# Append a register number
reg_no = input("Enter new register number to append: ")
mark = int(input("Enter mark for the register number: "))
rank_list[reg_no] = mark
print("Rank List after appending a register number:")
print(rank_list)

# Sort the register number based on marks
sorted_rank_list = dict(sorted(rank_list.items(), key=lambda item: item[1], reverse=True))
print("Rank List after sorting based on marks:")
print(sorted_rank_list)

# Create another set with name and sex
name_sex_set = set()
num_of_entries = int(input("Enter number of entries to add in Name and Sex set: "))
for i in range(num_of_entries):
    name = input(f"Enter name for entry {i+1}: ")
    sex = input(f"Enter sex for entry {i+1} (M/F): ")
    name_sex_set.add((name, sex))
print("Name and Sex Set:")
print(name_sex_set)

# Modify the second set
name = input("Enter name to add in Name and Sex set: ")
sex = input("Enter sex for the name (M/F): ")
name_sex_set.add((name, sex))
print("Name and Sex Set after modification:")
print(name_sex_set)

# Compare two sets and create a new set which is common on both sets
new_set_common = rank_list.keys() & set([name for name, sex in name_sex_set])
print("New set with common elements:")
print(new_set_common)

# Compare two sets and create a new set which is uncommon on both sets
new_set_uncommon = rank_list.keys() ^ set([name for name, sex in name_sex_set])
print("New set with uncommon elements:")
print(new_set_uncommon)

# Remove an item
reg_no = input("Enter register number to remove: ")
del rank_list[reg_no]
print("Rank List after removing an item:")
print(rank_list)

# Remove all the items
rank_list.clear()
print("Rank List after removing all items:")
print(rank_list)

# Delete the set
del name_sex_set
print("Name and Sex Set after deleting:")
try:
    print(name_sex_set) # This will throw a NameError as the set is deleted
except NameError as e:
    print(e)

# Add multiple items to the rank list
num_of_entries = int(input("Enter number of entries to add in Rank List: "))
for i in range(num_of_entries):
    reg_no = input(f"Enter register number for entry {i+1}: ")
    mark = int(input(f"Enter mark for entry {i+1}: "))
    rank_list[reg_no] = mark
print("Rank List after adding multiple items:")
print(rank_list)

# Get the top 3 ranks from the
