##1. write a program to print the number from 1 to 50
# for i in range (1,51):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz",end=" ")
#     elif i%3==0:
#         print("Fizz",end=" ")
#     elif i%5==0: 
#         print("Buzz",end=" ")
#     else:
#         print(i,end=" ")
        
##2. write a program to print all prime numbers between 1 and 100        
# for num in range (1,101):
#     if num>1:
#         prime=True
        
#         for i in range (2,num):
#             if num%i==0:
#                 prime =False
                
#         if prime:
#             print(num,end=" ")

##3. write a program that asks the user for a score between 0 and 100 and prints the corresponding grade based on the following criteria:
# score=int(input("enter a score btw 0 and 100"))
# if 0<= score <= 100:
#     if 90<= score<=100:
#         print("grade A")
#     elif 80<=score<=89:
#         print("grade B")
#     elif 70<=score<=79:
#         print("grade C")
#     elif 60<=score<=69:
#         print("grade D")
#     elif score<=60:
#         print("fail")
# else:
#     print("invalid score")


##4.write a program that prints the multiplication table for a given number .
# num=int(input("enter a number"))
# for i in range (1,11):
#     print(f"{num} * {i}={num*i}")
    
    
##5. write a program to create a list of the squares of the even numbers from 1 to 20.
# squares = [i**2 for i in range(1, 21) if i % 2 == 0]
# print(squares)


##6.write a program to check if a given year is a leap year.A year is a leap year if it is divisible by 4,but not by 100,unless it is divisible by 400.
# year=int(input("enter a year"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year,"is a leap year")
# else:
#     print(year,"is not leap year")


##7. write a program that takes the length of three sides of a triangle as input and determines the type of triangle (equilateral, isosceles, right angle, or scalene) .
# a=float(input("enter first side:"))
# b=float(input("enter second side:"))
# c=float(input("enter third side:"))
# #check if the sides form a triangle
# if (a+b>c) and (b+c>a) and (c+a>b):
# #check for equilateral triangle:
#     if a==b==c:
#         print("it is a equilateral triangle")
# # check for isosceles triangle
#     elif (a==b)or(b==c)or (a==c):
#         print("it is a isosceles triangle ")
# #check for right angle triangle
#     elif (a*a+b*b==c*c)or(a*a+c*c==b*b)or(b*b+c*c==a*a):
#         print("it is a right angle triangle")
#     else:
#         print("it is scalene triangle ")
# else:
#     print("given sides do not form a triangle")                        


##8. write a program that takes an integer input from the user and classifies it as positive , negative or zero.
# n=float(input("enter a number:"))
# if n<0:
#     print(n,"is negative ")
# elif n>0:
#     print(n,"is positive ")
# else:
#     print(n,"is zero")


##10. write a program that calculates the body mass index and categorizes it based on the following criteria:
# BMI=float(input("enter your weight"))
# if BMI<18.5:
#     print("underweight")
# elif (18.5<=BMI<24.9):
#     print("normal weight")
# elif (25<=BMI<29.9):
#     print("overweight")
# else:
#     print("obesity")


##11. write a program that takes an integer input representing a day of the week (1 for Monday, 2 for Tuesday, etc.) and prints the corresponding day name. 
# day=int(input("enter a number from (1-7):"))
# if day==1:
#     print("monday")
# elif day==2:
#     print("tuesday")
# elif day==3:
#     print("wednesday")
# elif day==4:
#     print("thursday")
# elif day==5:
#     print("friday")
# elif day==6:
#     print("saturday")
# elif day==7:
#     print("sunday")
# else:
#     print("invalid input! please enter input between 1-7")


##12. write a program that calculates the discount on a product based on the following criteria:
# price=float(input("enter the price"))
# if price>1000:
#     print("discount of 10% is applied")
# elif (500<price<1000):
#     print("discount of 5% is applied")
# else:
#     print("no discount")

    
##13. write a program to find the sum of the first n natural numbers .
# n=int(input("enter a number:"))
# sum=0
# for i in range (1,n+1):
#     sum+=i
# print("the sum of first",n,"natural numbers is:",sum)


##14.given a dictionary employee_details where the keys are employees IDs and values are dictionaries with name, department and salary ,filter and create a list of names of employees who have a salary greater than 50,000.
# employee_details = {
#     1: {"name": "Alice", "department": "HR", "salary": 60000},
#     2: {"name": "Ajit", "department": "IT", "salary": 45000},
#     3: {"name": "Rahul", "department": "Finance", "salary": 70000}}

# high_earners = [employee["name"] for employee in employee_details.values() if employee["salary"] > 50000]
# print("Employees with salary greater than 50,000:", high_earners)



##15. write a program to count the number of vowels in a given string.
# string = input("enter a string:")
# count=0
# for ch in string :
#     if ch in "aeiouAEIOU":
#         count+=1
# print("The number of vowels in the string is:", count)

 

##16.write a program to find the sum of all digits of a given number
# n = int(input("Enter a number: "))
# sum_of_digits=sum(int(digit) for digit in str(n))
# print("The sum of all digits of", n, "is:", sum_of_digits)


##17.write a program to print a pattern of stars :

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print("*" * i)
    


##18.write a program for a number guessing game where the computer randomly selects a number between 1 and 100,and the user tries to guess it.The program should give hints if the guess is too high or too low.

# import random
# secret_number = random.randint(1, 100)
# while True:
#     guess = int(input("Guess the number between 1 and 100: "))
    
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the number.")
#         break


##19.ask user to input a number and show all even number upto that number starting from number 1
# n = int(input("Enter a number: "))
# for i in range(2, n + 1, 2):
#     print(i,end=" " )



##20.write a program create a list of 10 elements(number elements)and perform the following 

# numbers = [10, 25, 30, 25, 40, 50, 60, 70, 80, 90]
# # a) Check if element 25 exists in the list
# if 25 in numbers:
#     print("Element 25 exists in the list.")
# else:
#     print("Element 25 does not exist in the list.")

# # b) Total length of the list
# print("Total length of the list:", len(numbers))

# # c) Total occurrence of 25 in the list
# print("Total occurrence of 25 in the list:", numbers.count(25))

# # d) Traverse each element in the list
# print("Traversing each element:")
# for element in numbers:
#     print(element)

# # e) Show all even numbers in the list
# print("Even numbers in the list:")
# for num in numbers:
#     if num % 2 == 0:
#         print(num, end=" ")
        
        
##21. ask user to input a string of min 10 words and max 19 words and perform the following :

# string = input("Enter a string with minimum 10 words and maximum 19 words: ")
# words = string.split()
# if len(words) < 10 or len(words) > 19:
#     print("Invalid input! Please enter a string with minimum 10 words and maximum 19 words.")
# else:
#     # 1. Print full string and length of string
#     print("Full string:", string)
#     print("Length of string:", len(string))

#     # 2. Check if the string is a palindrome
#     if string == string[::-1]:
#         print("The string is a palindrome.")
#     else:
#         print("The string is not a palindrome.")

#     # 3. Tell the middle word in the string
#     middle_index = len(words) // 2
#     print("Middle word in the string:", words[middle_index])

#     # 4. Print the second last word in the string
#     if len(words) >= 2:
#         print("Second last word in the string:", words[-2])
#     else:
#         print("Not enough words to determine the second last word.")


##22.perform the following task as per the output
#welcome to calci:
#1.power
#2.sum
#3.sub
#4. multiple

# print("Welcome to Calci:")
# print("1. Power")
# print("2. Sum")
# print("3. Sub")
# print("4. Multiple")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     num1 = int(input("Enter 1st Number: "))
#     num2 = int(input("Enter 2nd Number: "))
#     print("Power is", num1 ** num2)

# elif choice == 2:
#     num1 = int(input("Enter 1st Number for Sum: "))
#     num2 = int(input("Enter 2nd Number for Sum: "))
#     print("Sum is", num1 + num2)

# elif choice == 3:
#     num1 = int(input("Enter 1st Number for Sub: "))
#     num2 = int(input("Enter 2nd Number for Sub: "))
#     print("Subtraction is", num1 - num2)

# elif choice == 4:
#     num1 = int(input("Enter 1st Number for Multiple: "))
#     num2 = int(input("Enter 2nd Number for Multiple: "))
#     print("Multiplication is", num1 * num2)

# else:
#     print("Invalid Choice")


##23.write a python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings 
#input-- X=['abc','xyz','aba','1221']

# X = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for string in X:
#     if len(string) >= 2 and string[0] == string[-1]:
#         count += 1
# print("Number of strings with length 2 or more and same first and last character:", count)
