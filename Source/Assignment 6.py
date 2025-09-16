
# Questions for this assignment
# Write a program that takes three numbers as input and determines the largest number using if-elif-else.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 > num2 and num1 > num3:
    print(num1, "Is greater than ", num2 , "and ", num3)
elif num2 > num1 and num2 > num3:
    print(num2, "Is greater than ", num1 , "and ", num3)
elif num3 > num1 and num3 > num2:
    print(num3, "Is greater than ", num1 , "and ", num2)
else:
    print(num1, "Is greater than ", num2 , "and ", num3)

#2,3,4
#1>2 and 1>3
#2>1 and 2>3
#3>1 and 3>2 true

#largest number in array
numbers = [100, 24, 36, 400, 550]
largest = max(numbers);
smallest = min(numbers);
print(largest, smallest)
getLargestNumber = numbers[0]
for number in numbers:
    print(number)
    if number > getLargestNumber:
        print(number ,">", getLargestNumber)
        getLargestNumber = number
        print(getLargestNumber)

# Write a program that prints even numbers from 1 to 20 using a for loop and continue statement.

start = int(input("Enter a start number: "))
end = int(input("Enter an end number: "))

for number in range(start, end + 1):  # include 'end'
    if number % 2 != 0:  # if number is odd
        continue  # skip odd numbers
    print(number, "is even")

# Write a program that asks user for a number and checks if it lies between 10 and 50 using the and operator.

checkNumber = int(input("Enter a number: "))
if checkNumber > 10 and checkNumber < 50:
    print(checkNumber, "is between 10 and 50")
else:
    print(checkNumber, "is not between 10 and 50")

# Write a program that iterates through a list of  numbers = [12, 15, 22, 29, 35, 42, 50] and finds the first multiple of 7 (35) using a for loop and break statement.

numbersList = [12, 15, 22, 29, 35, 42, 50]
for number in numbersList:
    if number % 7 == 0:
        print("The first multiple of 7 is:", number)
        break

# Write a program that prints numbers from 10 to 1 using a while loop and the not operator.
i = 10;
while not (i < 1):
    print(i)
    i = i - 1


