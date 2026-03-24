#A. Python IF (Single Condition)

#1. Write a Python program to check if a number is positive. 
a = int(input("Enter a number: "))
if a > 0:
    print("Number is positive")


#2. Print "Eligible to vote" if age is 18 or above. 
Age = int(input("Enter Valid age : "))
if Age>18:
    print("Eligible to Vote")

#3. Check if a number is divisible by 7. 
num = int(input("Enter a number: "))
if num%7==0:
    print("Divisible by 7")

#4. Print "Pass" if marks are greater than 40.
marks = int(input("Enter marks :"))
if marks>40:
    print("Pass")

#5. Check if a number is greater than 100. 
num = int(input("Enter a number :"))
if num>100:
    print("Number is greater than hundered")
 
#6. Display a message if temperature exceeds 45°C. 
temp = int(input("Enter temp :"))
if temp>45:
    print("Temperature exceeds 45C")

#7. Check if a string length is more than 8 characters. 
text = input("Enter a string:")
if len(text)>8:
    print("String length is more than 8 characters")

#8. Print "Logged In" if password matches "admin123". 
password = input("Enter a password:")
if password == "admin123":
    print("Logged In")

#9. Check if a number is a multiple of 10. 
num = int(input("Enter a number:"))
if num%10 == 0:
    print("Number is a multiple of 10")

#10. Print a warning if balance is below minimum limit.
bal = int(input("Enter account balance:"))
if bal<=2000:
    print("Warning : Balance is below minimum limit")


#B. Python IF–ELSE (Two Conditions)

#11. Check whether a number is even or odd. 
num = int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")
    
#12. Find the largest of two numbers. 
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if a>b:
    print("Greater number is a")
else:
    print("Greater number is b")

#13. Check whether a person is eligible for driving license. 
Age = int(input("Enter person's age:"))
if Age>=18:
    print("Eligible for driving license")
else:
    print("Not Eligible")


#14. Print "Pass" or "Fail" based on marks.     
Marks = int(input("Enter marks:"))
if Marks>=40:
    print("Pass")
else:
    print("Fail")

#15. Check whether a number is positive or negative.
num = int(input("Enter a number:"))
if num>0:
    print("Positive")
else:
    print("Negative")

#16. Check whether a character is a vowel or consonant. 
ch = input("Enter a character:")
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonent")

#17. Check if a year is leap or not.
days  = int(input("Enter the no. of days in a year: "))
if days == 366:
    print("Leap year")
else:
    print("Not a leap year")

#18. Print "Valid Password" or "Invalid Password". 
password = input("Enter a password: ")
if password == "Admin123":
    print("Valid Password")
else:
    print("Invalid Password")

#19. Determine whether salary is taxable or not. 
salary = float(input("Enter salary : "))
if salary > 250000:
    print("Salary is taxable")
else:
    print("Not taxable")

#20. Check whether a number is greater than 50 or not. 
num = int(input("Enter a number: "))
if num >50:
    print("Number is greater than 50")
else:
    print("Not greater than 50")


#C. Python NESTED IF–ELSE 
 
#21. Find the largest of three numbers. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest is:", a)
    else:
        print("Largest is:", c)
else:
    if b > c:
        print("Largest is:", b)
    else:
        print("Largest is:", c)


#22. Check whether a number is positive, negative, or zero. 
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#23. Assign grades: 
#● A → marks ≥ 90 
#● B → marks ≥ 75 
#● C → marks ≥ 60 
#● Fail → below 60 
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
    
#24. Check whether a triangle is equilateral, isosceles, or scalene    
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
    

#25. Check whether a character is uppercase, lowercase, digit, or special character.               
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")    
 
#26. Calculate electricity bill using slab-wise rates. 
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("Bill =", bill)


#27. Validate login using username and password.
user = input("Username: ")
pwd = input("Password: ")

if user == "admin":
    if pwd == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")    
          

#28. Check student result using marks of 3 subjects.           
m1 = int(input("Marks 1: "))
m2 = int(input("Marks 2: "))
m3 = int(input("Marks 3: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Pass")
else:
    print("Fail")


#29. Find the second largest number among three numbers.           
a = int(input())
b = int(input())
c = int(input())

if (a > b and a < c) or (a < b and a > c):
    print("Second largest:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Second largest:", b)
else:
    print("Second largest:", c)        
            
#30. Check loan eligibility using age, salary, and credit score. 
age = int(input("Age: "))
salary = int(input("Salary: "))
score = int(input("Credit score: "))

if age >= 21:
    if salary >= 20000:
        if score >= 700:
            print("Eligible for loan")
        else:
            print("Low credit score")
    else:
        print("Low salary")
else:
    print("Age not eligible")

    
#D. Python ELIF (Multiple Conditions)

#31. Print day name using day number (1–7).
day = int(input("Enter day number: "))

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Invalid")

#32. Print month name using month number.          
m = int(input("Enter month number: "))

months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

if 1 <= m <= 12:
    print(months[m-1])
else:
    print("Invalid")

#33. Display grade based on percentage. 
p = int(input("Enter percentage: "))

if p >= 90:
    print("A")
elif p >= 75:
    print("B")
elif p >= 60:
    print("C")
else:
    print("Fail")
    
#34. Display bonus percentage based on experience years. 
exp = int(input("Years of experience: "))

if exp >= 10:
    print("20% bonus")
elif exp >= 5:
    print("10% bonus")
else:
    print("No bonus")

#35. Identify traffic signal meaning. 
color = input("Enter signal color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Invalid")

#36. Categorize temperature as Cold / Warm / Hot.     
t = int(input("Temperature: "))

if t < 20:
    print("Cold")
elif t <= 35:
    print("Warm")
else:
    print("Hot")

#37. Categorize employee based on salary range.
sal = int(input("Salary: "))

if sal < 20000:
    print("Low income")
elif sal <= 50000:
    print("Middle income")
else:
    print("High income")


#38. Print discount percentage based on purchase amount.
amt = int(input("Purchase amount: "))

if amt >= 5000:
    print("20% discount")
elif amt >= 2000:
    print("10% discount")
else:
    print("No discount")


#39. Identify number type: single-digit / double-digit / multi-digit.

n = abs(int(input("Enter number: ")))
digits = len(str(n))
if digits == 1:
    print("Single digit")
elif digits == 2:
    print("Double digit")
else:
    print("Multi digit")


#40. Assign performance rating: Poor / Average / Good / Excellent.

score = int(input("Performance rating : "))
if score < 40:
    print("Poor")
elif score < 60:
    print("Average")
elif score < 80:
    print("Good")
else:
    print("Excellent")
    

#E. Python COMPLEX CONDITIONS (AND / OR / NOT)

#41. Check whether a number is divisible by 5 and 11.

n = int(input())
if n % 5 == 0 and n % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible")


#42. Check if a person is eligible for loan: 
#● age ≥ 21 
#● salary ≥ 25,000 
#● credit score ≥ 700

age = int(input())
salary = int(input())
score = int(input())
if age >= 21 and salary >= 25000 and score >= 700:
    print("Eligible")
else:
    print("Not eligible")


#43. Validate login using username AND password.

user = input()
password = input()

if user == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


#44. Check student pass condition: 
#● All subjects ≥ 40 
#● Average ≥ 50

m1 = int(input())
m2 = int(input())
m3 = int(input())
avg = (m1 + m2 + m3) / 3
if m1 >= 40 and m2 >= 40 and m3 >= 40 and avg >= 50:
    print("Pass")
else:
    print("Fail")

#45. Check if a number lies between 10 and 100.

n = int(input())
if 10 <= n <= 100:
    print("Between 10 and 100")
else:
    print("Not in range")


#46. Check exam eligibility: 
#● attendance ≥ 75% OR 
#● medical certificate available

att = int(input("Attendance: "))
medical = input("Medical certificate (yes/no): ")
if att >= 75 or medical == "yes":
    print("Eligible")
else:
    print("Not eligible")


#47. Validate a date using conditions.

d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))
if 1 <= m <= 12 and 1 <= d <= 31:
    print("Valid date")
else:
    print("Invalid date")

#48. Check whether an email format is valid.

email = input("Enter email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


#49. Determine insurance eligibility using age, health status, and income.

age = int(input())
health = input("Health good? (yes/no): ")
income = int(input())
if age < 60 and health == "yes" and income >= 20000:
    print("Eligible for insurance")
else:
    print("Not eligible")


#50. Check leap year using complete leap year logic.

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS

#51. Write a Python program to calculate income tax using slabs.

income = float(input("Enter your income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax =", tax)

 
#52. Create an ATM withdrawal program with balance checks.

balance = 10000
amount = float(input("Enter withdrawal amount: "))
if amount <= balance:
    balance = balance - amount
    print("Transaction successful")
    print("Remaining balance =", balance)
else:
    print("Insufficient balance")

#53. Check promotion eligibility using experience and performance.

experience = int(input("Enter years of experience: "))
performance = input("Performance (good/average): ")
if experience >= 5 and performance == "good":
    print("Eligible for Promotion")
else:
    print("Not Eligible")

    
#54. Implement a grading system using nested if–else.

marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Division")
    else:
        print("Pass")
else:
    print("Fail")
    
#55. Validate strong password using multiple conditions.

password = input("Enter password: ")
if len(password) >= 8:
    if any(c.isdigit() for c in password):
        if any(c.isupper() for c in password):
            print("Strong Password")
        else:
            print("Add uppercase letter")
    else:
        print("Add a number")
else:
    print("Password too short")

    
#56. Calculate delivery charges based on location and order amount.

location = input("Enter location (local/outstation): ")
amount = float(input("Enter order amount: "))

if location == "local":
    if amount >= 500:
        charge = 0
    else:
        charge = 50
else:
    charge = 100

print("Delivery charge =", charge)


#57. Determine online exam qualification.

attendance = int(input("Enter attendance %: "))
fees_paid = input("Fees paid? (yes/no): ")
if attendance >= 75 and fees_paid == "yes":
    print("Eligible for Exam")
else:
    print("Not Eligible")

    
#58. Create movie ticket pricing logic based on age & show time.

age = int(input("Enter age: "))
time = input("Show time (day/night): ")
if age < 12:
    price = 100
elif age >= 60:
    price = 120
else:
    if time == "night":
        price = 200
    else:
        price = 150

print("Ticket price =", price)

#59. Determine bank account type based on balance.

balance = float(input("Enter balance: "))
if balance >= 100000:
    print("Premium Account")
elif balance >= 10000:
    print("Savings Account")
else:
    print("Basic Account")
    
#60. Create a menu-driven program using if–elif–else.

print("1. Add")
print("2. Subtract")
print("3. Multiply")

choice = int(input("Enter choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
else:
    print("Invalid choice")



