#Part 1 – Basic Level

#1. Print numbers from 1 to 10 using a while loop.

i = 1
while i <= 10:
    print(i)
    i = i + 1

    
#2. Print even numbers from 1 to 20.

i = 2
while i <= 20:
    print(i)
    i = i + 2

#3. Print odd numbers from 1 to 20.

i = 1
while i <= 20:
    print(i)
    i = i + 2
    
#4. Print numbers from 10 to 1 (reverse order).

i = 10
while i >= 1:
    print(i)
    i = i - 1
    
#5. Print multiplication table of 5 using while loop.

i = 5
while i <= 50:
    print(i)
    i = i + 5


#Part 2 – Intermediate Level

#6. Find the sum of first 10 natural numbers using while loop.

i = 1
sum = 0

while i <= 10:
    sum = sum + i
    i = i + 1

print("Sum =", sum)


#7. Find factorial of a number entered by user.

num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)

#8. Count number of digits in a given number.
a = int(input("Enter a number : "))
count = 0
while a > 0:
    a = a // 10
    count = count + 1
    print("Digits = ", count)
#9. Reverse a number using while loop.
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse =", rev)
    
#10. Check whether a number is palindrome or not using while loop.
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#Part 3 – Pattern Based 
#11. Print pattern:
"""
* 
** 
*** 
**** 
*****
"""
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1

    
#12. Print pattern:
"""
1 
12 
123 
1234 
12345
"""
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1

    
#Part 4 – Logical / Real Scenario
    
#13. Ask user to enter password until correct password is entered.
correct = "1234"
password = ""

while password != correct:
    password = input("Enter password: ")

print("Access Granted")

#14. Create a number guessing game: 
#• Generate a random number (1–10) 
#• Keep asking user until they guess correctly
import random

num = random.randint(1, 10)
guess = 0

while guess != num:
    guess = int(input("Guess number (1-10): "))

print("Correct Guess!")

#15. Keep taking input numbers until user enters 0, then print total sum.
sum = 0
num = 1

while num != 0:
    num = int(input("Enter number: "))
    sum = sum + num

print("Total =", sum)


#Bonus Challenge (Interview Level)


#16. Print Fibonacci series up to N terms using while loop.
n = int(input("Enter terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1

    
#17. Check whether a number is Armstrong number.
num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")

    
#18. Print prime numbers between 1 to 50 using while loop.

i = 2
while i <= 50:
    j = 2
    is_prime = True

    while j < i:
        if i % j == 0:
            is_prime = False
            break
        j = j + 1
    if is_prime:
        print(i)
    i = i + 1    
