"""
PART 1 - BASIC FOR LOOP QUESTIONS

Q1. Print Numbers 
Use a for loop to print numbers from 1 to 10.
"""

for i in range(1,11):
    print(i)

"""    
Q2. Print Even Numbers 
Print all even numbers between 1 and 20.
"""

for i in range(2,21,2):
    print(i)

"""
Q3. Find Sum 
Print the sum of n1
umbers from 1 to 10 using a for loop.     
"""

sum = 0
for i in range(1,11,1):
    sum = sum + i
print("Sum =",sum)

"""
Q4. Multiplication Table 
Take a number from the user and print its multiplication table up to 10.

sol :-  print(num, "x", i, "=", num*i)
"""

num = int(input("Enter a number : "))
for i in range(1,11):
    table = num*i
    print(num, "x", i, "=", table)

"""
Q5. Count Characters 
Take a string and count the total number of characters using a for loop. 
"""
text = input("Enter a string : ")
count = 0
for ch in text:
    count = count + 1
    print("Total number of characters = ",count)

"""
PART 2 - BREAK RELATED QUESTIONS

Q6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5. 
"""

for i in range(1,11,1):
    if i == 5:
        break
    print(i)
    
"""
Q7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop.
"""

num = [10,15,25,30,35,40]
for n in num:
    if n == 25:
        print("Found")
        break
    
"""
Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop. 
"""    


"""
PART 3 - CONTINUE RELATED QUESTIONS

Q9. Skip 5 
Print numbers from 1 to 10. 
Skip number 5.
"""

for i in range(1,11):
    if i == 5:
        continue
    print(i)

"""
Q10. Skip Even Numbers 
Print numbers from 1 to 20. 
Skip all even numbers.
"""

for i in range(1,21):
    if i%2==0:
        continue
    print(i)

"""
Q11. Skip Letter 
Print each character of the string "PYTHON". 
Skip the letter "O".
"""

s = "PYTHON"
for ch in s:
    if  ch == "O":
        continue   
    print(ch)

"""
PART 4 – Pass Related Questions

Q12. Empty Loop 
Run a loop from 1 to 5 but do nothing inside the loop using pass. 
"""

for i in range(1,6,1):
    pass

"""
Q13. Skip Using Pass 
Loop from 1 to 10. 
If number is 6, just use pass. 
"""

for i in range(1,11):
    if i == 6:
        pass
    print(i)

"""
PART 5 – For-Else Questions 
(Remember: else runs only if the loop is not stopped by break.) 
"""
"""
Q14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found".
"""

num = [25,50,75,100,125,150]
for n in num:
    if n == 100:
        print("Found")
        break
else:
    print("Not Found")

"""
Q15. Prime Number Check 
Take a number from the user and check whether it is prime using for-else.   
"""
    
num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")


"""
PART 6 – Pattern Questions   
"""
"""
Q16. Star Pattern 
Print: 
* 
** 
*** 
**** 
*****
"""

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = "")
    print()

"""
Q17. Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
*
"""
for i in range(5, 0, -1):
    print("*" *i)

"""
Q18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = "")
    print()

"""
Q19. Same Number Pattern 
Print: 
1 
22 
333 
4444
55555
"""

for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
        
"""   
Q20. Pyramid Pattern 
Print: 
      * 
     *** 
    ***** 
   ******* 
  *********
"""
 
    
n = 5

for i in range(1, n + 1):
    
    for s in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()  
