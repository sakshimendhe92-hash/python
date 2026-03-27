# Q1: Create a Pandas DataFrame by reading "books.csv"
# Perform operations like report, filtering, cheapest/costliest, sorting

import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("\n--- Complete Book Report ---")
print(df)

# b) Print list of books of a given author
author_name = input("\nEnter author name: ")
print("\nBooks by", author_name)
print(df[df['author'] == author_name])

# c) Print list of books of a given publisher
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by publisher", publisher_name)
print(df[df['publisher'] == publisher_name])

# d) Print cheapest and costliest book
cheapest = df[df['price'] == df['price'].min()]
costliest = df[df['price'] == df['price'].max()]

print("\nCheapest Book:")
print(cheapest)

print("\nCostliest Book:")
print(costliest)

# e) Sort by year of publication
print("\nBooks sorted by year:")
print(df.sort_values(by='year'))