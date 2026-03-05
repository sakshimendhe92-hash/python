# Take input from user
nums = input("Enter integers separated by space: ")

# Convert input string into tuple of integers
t = tuple(map(int, nums.split()))

# a) Print total number of items
print("Total number of items:", len(t))

# b) Print last item
print("Last item in tuple:", t[-1])

# c) Print tuple in reverse order
print("Tuple in reverse order:", t[::-1])

# d) Check if integer 5 is present
if 5 in t:
    print("Yes, 5 is present in the tuple.")
else:
    print("No, 5 is not present in the tuple.")

# e) Remove first and last items, sort remaining items
if len(t) > 2:
    new_tuple = t[1:-1]          # Remove first and last
    sorted_tuple = tuple(sorted(new_tuple))  # Sort
    print("After removing first and last items and sorting:", sorted_tuple)
else:
    print("Not enough elements to remove first and last items.")