#1. Write a program to print "Hello Python" on the screen. 
print("Hello Python")

#2. Write a program to take your name as input and print "Hello <name>".
name = input("Enter the name : ")
print("Hello" , name)

#3. Write a program to take one integer input from the user and print it. 
a = int(input("Enter an interger : "))
print("Entered Integer value :", a)


#4. Write a program to take two integers as input and print their sum. 
a = int(input("Enter 1st value :"))
b = int(input("Enter 2nd value :"))
print("You Entered : ", a + b)

#5. Write a program to take two integers as input and print their multiplication. 
a = int(input("Enter 1st value :"))
b = int(input("Enter 2nd value :"))
print("You Entered : ", a * b)

#6. Write a program to take one float number as input and print it. 
num = float(input("Enter the number : "))
print("You entered : ", num)

#7. Write a program to take two float numbers as input and print their average.
#hint :- To calculate the average of two float numbers : average = (a+b)/2

a = float(input("Enter 1st value : "))
b = float(input("Enter 2nd value : "))
average = (a+b)/2
print("Average : ", average)


#8. Write a program to take length and width (float) from the user and calculate the area of 
a rectangle.
l = float(input("Enter the length of the rectangle : "))
w = float(input("Enter the width of the rectangle : "))
area = l*w
print("Area of the rectangle :", area)


#9. Write a program to take an integer input and convert it into float, then print it. 
num = int(input("Enter an interger : "))
num = float(num)
print("Float num :", num)

#10. Write a program to take price of three items (float) and print the total price.
A = float(input("Enter the price of A item : "))
B = float(input("Enter the price of B item : "))
C = float(input("Enter the price of C item : "))
total_price = A+B+C
print("Total Price :", total_price)
