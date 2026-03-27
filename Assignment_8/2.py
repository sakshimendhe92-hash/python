# Q2: Create table of 5 states with name, area, population
# Generate reports like largest area, largest population, population density

import pandas as pd

# Taking input for 5 states
data = []

for i in range(5):
    print(f"\nEnter details for State {i+1}")
    name = input("State Name: ")
    area = float(input("Area: "))
    population = int(input("Population: "))
    
    data.append([name, area, population])

# Create DataFrame
df = pd.DataFrame(data, columns=["State", "Area", "Population"])

# a) Print complete information
print("\n--- State Information ---")
print(df)

# b) State with largest area
largest_area = df[df['Area'] == df['Area'].max()]
print("\nState with Largest Area:")
print(largest_area)

# c) State with largest population
largest_pop = df[df['Population'] == df['Population'].max()]
print("\nState with Largest Population:")
print(largest_pop)

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']
print("\n--- Population Density ---")
print(df)

# e) State with highest population density
highest_density = df[df['Density'] == df['Density'].max()]
print("\nState with Highest Population Density:")
print(highest_density)