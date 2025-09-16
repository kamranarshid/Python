#concat
firstName = "Kamran"
lastName = "Arshad"

fullName =  firstName + " " + lastName
print(fullName)

#repeation

word = "Hello "
print(word * 3)

#equality

fruit1 = "apple"
fruit2 = "apple"
# print(fruit1 + fruit2)
# print(fruit1 == fruit2)
# print(fruit1 != fruit2)
# print(fruit1 > fruit2)
# print(fruit1 < fruit2)
# print(fruit1 >= fruit2)
# print(fruit1 <= fruit2)

#membership operators
sentance ="a quick brown fox jumped over the lazy dog"
print('quick2' in sentance)

#string slicing

print(sentance[0:10]);
print(sentance[:5]);
print(sentance[:]);
# Exam2

#Take two numbers as input and compute their remainder using the modulus operator (%).

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
#mod

result = num1%num2
print(result)

# Write a program to check if a number entered by the user is greater than, less than, or equal to 10.

num3 = int(input("Enter third Number: "))
CheckValueWIth = 10
if num3 <= CheckValueWIth:
    print("Number is less than or equal to 10")
elif num3 >= CheckValueWIth:
    print("Number is greater than or equal to 10")
elif num3 == CheckValueWIth:
    print("Number is greater than or equal to 10")

# Write a program to check if a number is between 1 and 100 using the and operator.
num4 = int(input("Enter fourth Number: "))
if num4 <= 100 and num4 >= 1:
    print("Number is in between 1 to 100")
else:
    print("Number is not in between 1 to 100")

# Write a program to check if a number is not negative using the not operator.
num5 = int(input("Enter fifth Number: "))
if not num5 < 0:
    print("Number is not negative")
else:
    print("Number is negative")

# Take a number as input and increase it by 5 using the += operator. Then multiply it by 2 using the *= operator.
num6 = int(input("Enter sixth Number: "))

num6 += 5
print(num6)
num6 *= 2
print(num6)




