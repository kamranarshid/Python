# Write a program that takes a list of numbers and finds the maximum and minimum values.
# numbers = [10, 25, 8, 99, 3, 67]
# Hint: Use in-built functions min() and max()
#
myList = [10, 25, 8, 99, 3, 67]
print(myList)
myList.sort();
print(myList)
myList.reverse();
print(myList)

#max and min
Max = max(myList);
print(Max);
min = min(myList);
print(min);


#----------------------------------------------------------\
#Write a program that counts how many times a specific number appears in a tuple.
# Define the tuple
numbers = (2, 5, 3, 5, 8, 5, 10)

# Take input from user and convert to int
target = int(input("Enter a number: "))

# Check if number exists in tuple
if target in numbers:
    count = numbers.count(target)
    print(f"The number {target} appears {count} times in the tuple.")
else:
    print(f"The number {target} is not in the tuple.")

# Create a dictionary with some student names and their scores.Then,
# add a new student and remove an existing student. students = {"Alice": 85, "Bob": 78, "Charlie": 92}

students = {"Alice": 85, "Bob": 78, "Charlie": 92}
students["kamran"] = 70;
print(students)
del students["kamran"];
print(students)


# Given two sets of numbers, find:
# 1. Union (all unique elements from both sets)
# 2. Intersection (common elements)
# 3. Difference (elements in the first set but not in the second)
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1|set2;
print(union)
Intersection = set1 & set2;
print(Intersection)
difference = set1 - set2;
print(difference)

