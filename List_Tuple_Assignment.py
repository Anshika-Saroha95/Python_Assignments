# ---------------------- LIST QUESTIONS ----------------------

Python Programming Questions – LIST 
Basic Level 
#1. Write a Python program to create a list of integers and print its elements. 
lst = [1, 2, 3, 4, 5]
for i in lst:
    print(i)

#2. Write a program to find the sum and average of all elements in a list. 
lst = [1, 2, 3, 4, 5]
total = 0
for i in lst:
    total += i
avg = total / len(lst)
print("Sum:", total, "Average:", avg)

# 3. Write a program to find the largest and smallest element in a list. 
lst = [10, 5, 8, 20, 3]
print("Max:", max(lst), "Min:", min(lst))

# 4. Write a Python program to count the number of elements in a list without using len(). 
lst = [1, 2, 3, 4]
count = 0
for i in lst:
    count += 1
print("Count:", count)

# 5. Write a program to reverse a list without using built-in functions.
lst = [1, 2, 3, 4]
rev = []
for i in lst:
    rev = [i] + rev
print(rev)

# 6. Write a program to check if an element exists in a list. 
lst = [1, 2, 3]
x = 2
if x in lst:
    print("Exists")

# 7. Write a Python program to remove duplicate elements from a list.
lst = [1, 2, 2, 3, 3, 4]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)

#8. Write a program to sort a list in ascending and descending order. 
lst = [4, 1, 3, 2]
print(sorted(lst))
print(sorted(lst, reverse=True))

# Intermediate Level 
9. Write a program to merge two lists and remove duplicates. 
a = [1, 2, 3]
b = [3, 4, 5]
print(list(set(a + b)))

# 10. Write a program to find common elements between two lists. 
a = [1, 2, 3]
b = [2, 3, 4]
print([i for i in a if i in b])

# 11. Write a program to split a list into even and odd numbers. 
lst = [1, 2, 3, 4, 5]
even = [i for i in lst if i % 2 == 0]
odd = [i for i in lst if i % 2 != 0]
print(even, odd)

# 12. Write a program to rotate a list by n positions
lst = [1, 2, 3, 4, 5]
n = 2
print(lst[n:] + lst[:n])

# 13. Write a Python program to find the second largest number in a list. 
lst = [10, 20, 4, 45, 99]
lst.remove(max(lst))
print(max(lst))

# 14. Write a program to flatten a nested list. 
nested = [[1, 2], [3, 4], [5]]
flat = []
for sub in nested:
    for i in sub:
        flat.append(i)
print(flat)

# 15. Write a program to count frequency of each element in a list. 
lst = [1, 2, 2, 3, 3, 3]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print(freq)

# 16. Write a program to replace all negative numbers with zero in a list. 
lst = [1, -2, 3, -4]
lst = [i if i >= 0 else 0 for i in lst]
print(lst)

# Advanced Level 
#17. Write a program to remove all occurrences of a given element from a list. 
lst = [1, 2, 3, 2, 4]
x = 2
lst = [i for i in lst if i != x]
print(lst)

# 18. Write a program to check if a list is a palindrome. 
lst = [1, 2, 3, 2, 1]
print(lst == lst[::-1])

# 19. Write a Python program to find missing numbers in a given list of consecutive integers.
lst = [1, 2, 4, 6]
missing = []
for i in range(lst[0], lst[-1]):
    if i not in lst:
        missing.append(i)
print(missing)

# 20. Write a program to perform element-wise addition of two lists.  
a = [1, 2, 3]
b = [4, 5, 6]
res = [a[i] + b[i] for i in range(len(a))]
print(res)

# 21. Write a Python program to find the longest increasing subsequence in a list.
lst = [3, 10, 2, 1, 20]
lis = []
for i in lst:
    if not lis or i > lis[-1]:
        lis.append(i)
print(lis)

# 22. Write a program to group elements based on frequency. 
lst = [1, 2, 2, 3, 3, 3]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print(sorted(lst, key=lambda x: freq[x]))

# ---------------------- TUPLE QUESTIONS ----------------------

# Basic Level 
#23. Write a Python program to create a tuple and print its elements. 
t = (1, 2, 3)
print(t)

# 24. Write a program to find the length of a tuple. 
t = (1, 2, 3)
print(len(t))

# 25. Write a program to find the maximum and minimum element in a tuple.
t = (5, 2, 8, 1)
print(max(t), min(t))

# 26. Write a program to convert a tuple into a list. 
t = (1, 2, 3)
lst = list(t)
print(lst)

# 27. Write a program to check if an element exists in a tuple. 
t = (1, 2, 3)
print(2 in t)

# 28. Write a program to count occurrences of an element in a tuple. 
t = (1, 2, 2, 3)
print(t.count(2))

# Intermediate Level 
#29. Write a program to slice a tuple and display the result. 
t = (1, 2, 3, 4, 5)
print(t[1:4])

# 30. Write a program to find repeated elements in a tuple. 
t = (1, 2, 2, 3, 3)
print(set([i for i in t if t.count(i) > 1]))

# 31. Write a program to merge two tuples. 
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# 32. Write a program to unpack elements of a tuple into variables. 
t = (1, 2, 3)
a, b, c = t
print(a, b, c)

# 33. Write a Python program to sort a tuple. 
t = (3, 1, 2)
print(tuple(sorted(t)))

# 34. Write a program to convert a list of tuples into a dictionary.
lst = [(1, 'a'), (2, 'b')]
d = dict(lst)
print(d)

# Advanced Level 
#35. Write a program to find the index of an element in a tuple. 
t = (10, 20, 30)
print(t.index(20))

# 36. Write a program to remove an element from a tuple (without directly modifying it).
t = (1, 2, 3, 4)
lst = list(t)
lst.remove(3)
t = tuple(lst)
print(t)

# 37. Write a program to find common elements between two tuples. 
t1 = (1, 2, 3)
t2 = (2, 3, 4)
print(tuple(set(t1) & set(t2)))

# 38. Write a Python program to check if a tuple is a palindrome. 
t = (1, 2, 3, 2, 1)
print(t == t[::-1])

# 39. Write a program to find the element with maximum frequency in a tuple. 
t = (1, 2, 2, 3, 3, 3)
freq = {}
for i in t:
    freq[i] = freq.get(i, 0) + 1
print(max(freq, key=freq.get))

# 40. Write a program to create a nested tuple and access its elements. 
t = ((1, 2), (3, 4))
print(t[0][1])  
