# ==============================
# Practical 11 - Lab Assignment 2
# ==============================

import matplotlib.pyplot as plt

# Q2: Input recruitment data of companies

companies = ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "Amdocs"]

recruitments = []

print("Enter number of recruitments for each company:")
for c in companies:
    val = int(input(f"{c}: "))
    recruitments.append(val)

# a) Bar Chart
plt.figure()
plt.bar(companies, recruitments)
plt.title("Recruitment Comparison (Bar Chart)")
plt.xlabel("Companies")
plt.ylabel("No. of Recruitments")
plt.xticks(rotation=30)
plt.show()


# b) Pie Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct="%1.1f%%")
plt.title("Recruitment Distribution (Pie Chart)")
plt.show()


# c) Customize Pie Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct="%1.1f%%",
        shadow=True, startangle=140)
plt.title("Customized Pie Chart")
plt.show()


# d) Doughnut Chart

plt.figure()
plt.pie(recruitments, labels=companies, autopct="%1.1f%%")

# Draw circle for doughnut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Doughnut Chart")
plt.show()


# e) Compare IBM & Amdocs

ibm = recruitments[companies.index("IBM")]
amdocs = recruitments[companies.index("Amdocs")]

plt.figure()
plt.bar(["IBM", "Amdocs"], [ibm, amdocs])
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("No. of Recruitments")
plt.show()