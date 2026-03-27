# Lab Assignment 2
# Develop a program to copy contents of a Python script into another file without comments.
# Ask user for source and destination file names and print contents of both files.

# Taking input from user
source_file = input("Enter source Python file name: ")
destination_file = input("Enter destination file name: ")

try:
    with open(source_file, 'r') as file1:
        lines = file1.readlines()

    new_lines = []

    # Removing comments
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line.startswith('#') and stripped_line != "":
            new_lines.append(line)

    # Writing to destination file
    with open(destination_file, 'w') as file2:
        file2.writelines(new_lines)

    print("\nFile copied successfully without comments!")

    # Printing contents of source file
    print("\n--- Source File Content ---")
    with open(source_file, 'r') as file1:
        print(file1.read())

    # Printing contents of destination file
    print("\n--- Destination File Content ---")
    with open(destination_file, 'r') as file2:
        print(file2.read())

except FileNotFoundError:
    print("Error: Source file not found.")