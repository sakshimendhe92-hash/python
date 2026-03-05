# Take input from user
prices = input("Enter prices separated by space: ")

# Convert input string into tuple of integers
price_tuple = tuple(map(int, prices.split()))

# a) Print total number of items sold
print("Total number of items sold:", len(price_tuple))

# b) Print price of cheapest item
print("Cheapest item price:", min(price_tuple))

# c) Print price of costliest item
print("Costliest item price:", max(price_tuple))

# d) Print price list in ascending order
sorted_prices = tuple(sorted(price_tuple))
print("Prices in ascending order:", sorted_prices)

# e) Print number of costliest items sold
costliest = max(price_tuple)
count_costliest = price_tuple.count(costliest)
print("Number of costliest items sold:", count_costliest)