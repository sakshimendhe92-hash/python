# Lab Assignment 1
# Write a program that reads a text file and writes its contents into a new file in uppercase.

# Taking input from user
source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    # Open source file in read mode
    with open(source_file, 'r') as file1:
        content = file1.read()

    # Convert content to uppercase
    upper_content = content.upper()

    # Write to destination file
    with open(destination_file, 'w') as file2:
        file2.write(upper_content)

    print("\nFile copied successfully with uppercase content!")

except FileNotFoundError:
    print("Error: Source file not found.")