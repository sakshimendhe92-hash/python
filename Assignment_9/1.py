# ==============================
# Practical 11 - Lab Assignment 1
# ==============================

import matplotlib.pyplot as plt

# Q1: Import sales data of a Cosmetic Company (taking input from user)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

total_profit = []

print("Enter total profit for each month:")
for m in months:
    profit = int(input(f"{m}: "))
    total_profit.append(profit)

# a) Read total profit and visualize using Line Plot
plt.figure()
plt.plot(months, total_profit, marker='o')
plt.title("Monthly Profit")
plt.xlabel("Months")
plt.ylabel("Profit")
plt.grid()
plt.show()


# b) Read all product sales data and show using Multiline Plot

products = ["Face Cream", "Face Wash", "Toothpaste", "Bathing Soap"]

sales_data = {}

for product in products:
    print(f"\nEnter sales for {product}:")
    sales = []
    for m in months:
        val = int(input(f"{m}: "))
        sales.append(val)
    sales_data[product] = sales

# Multiline Plot
plt.figure()
for product in products:
    plt.plot(months, sales_data[product], marker='o', label=product)

plt.title("Product Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()


# c) Show Face Cream and Face Wash using Bar Chart

fc = sales_data["Face Cream"]
fw = sales_data["Face Wash"]

x = range(len(months))

plt.figure()
plt.bar(x, fc, width=0.4, label="Face Cream")
plt.bar([i + 0.4 for i in x], fw, width=0.4, label="Face Wash")

plt.xticks([i + 0.2 for i in x], months)
plt.title("Face Cream vs Face Wash Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.show()


# d) Total yearly sales for each product using Pie Chart

total_sales = [sum(sales_data[p]) for p in products]

plt.figure()
plt.pie(total_sales, labels=products, autopct="%1.1f%%")
plt.title("Yearly Sales Distribution")
plt.show()