#      String Programming Questions

#ques1. Write a program to count the number of vowels in a string.

##str=input("enter the string:")
##count=0
##for ch in str:
##    if ch in "AIEOUaeiou":
##        count+=1
##print("number of vowel",count)

#ques2.Reverse a string without using built-in functions.


##str=input("enter the string:")
##rev=""
##for ch in str:
##    rev=ch+rev
##print("reverse string",rev)

#ques3. Check whether a string is a palindrome.
##str=input("enter the str:")
##rev=str[::-1]
##if str==rev:
##    print("string is palindrome")
##else:
##    print("string is not palindrome")

#ques4.Count uppercase and lowercase letters in a string.

##str=input("enter the string:")
##uppercase=""
##lowercase=""
##
##for ch in str:
##    if ch.isupper():
##        uppercase+=ch
##    elif ch.islower():
##            lowercase+=ch
##print("uppercase",uppercase)
##print("lowercase",lowercase)

#ques5.Replace all spaces in a string with _.

##str="I am harsh rathi"
##print(str.replace(" ","_"))

#                                    Intermediate

#ques6.Find the frequency of each character in a string.

##str1=input("enter the string:")
##freq=""
##for ch in str1:
##    if ch in freq:
##        freq[ch]+=1
##    else:
##        freq[ch]=1
##print(freq)

#ques7.  Remove duplicate characters from a string.

##str1=input("enter the string:")
##freq=""
##for ch in str1:
##    if ch not in freq:
##        freq+=ch
##print(freq)

#ques8.  Find the first non-repeating character in a string.

##str1=input("enter the string:")
##freq={}
##for ch in str1:
##    freq[ch]=freq.get(ch,0)+1
##for ch in str1:
##    if freq[ch]==1:
##        print("first non-repeating character is:",ch)
##        break
##else:
##    print("non-repeating character found")

#ques9. Check if two strings are anagrams.

##str1=input("enter the string 1:")
##str2=input("enter the string 2:")
##sorted_list1=sorted(str1)
##sorted_list2=sorted(str2)
##if sorted_list1==sorted_list2:
##    print("string are anagrams")
##else:
##    print("string are not anagrams")

#ques 10. Convert "hello world" → "Hello World" (title case without using .title()).
##
##str1="hello world"
##words=str1.split()
##result=""
##for word in words:
##    new_word=word[0].upper()+word[1:]
##    
##    result+=new_word+""
##print(result.strip())


                        #TRICKY QUESTIONS
#ques 11.Compress a string like "aaabbc" → "a3b2c1".

##str1=input("enter the string:")
##result=""
##count=1
##for i in range (len(str1)-1):
##    if str1[i]==str1[i+1]:
##        count+=1
##    else:
##        result+=str1[i]+str(count)
##        count=1
##result+=str1[-1]+str
##(count)
##print(result)

#ques 12.  Rotate a string left by n positions.

##str1=input("enter the string:")
##n=int(input("no of time you want to rotate string:"))
##n=n%len(str1)
##result=str1[n:]+str1[:n]
##print("orignal",str1)
##print("result",result)



#                     Set Programming Questions

#Basic 
#1. Create a set and add elements dynamically.

##set1={10,20,30,10}
##set1.add(100)
##set1.add(200)
##print(set1)

#2. Find the union and intersection of two sets.

##set1={10,30,40,30,10}
##set2={50,30,320,13}
##set3=set1|set2
##print(set3)

#3. Remove duplicate elements from a list using a set.

##a=[10,40,30,40,23,5,34]
##print(set(a))

#4. Check if an element exists in a set.

##set1={10,2,3,420,45}
##element=int(input("enter the number:"))
##if element in set1:
##    print("element exist")
##else:
##    print("element not exist")

#5. Find the difference between two sets.

##set1={10,20,3,4,5,23,45}
##set2={43,32,2,45,6,531,}
##diff=set1-set2
##print("difference",diff)


#                           Intermediate

#1.Find common elements in two lists using sets.

##set1={10,20,30,40,50}
##set2={30,40,50,60,70}
##set3=set1&set2
##print(set3)

#2. Check whether one set is a subset of another.

##set1={1,2,3,4,5}
##set2={1,2,3,4,5,6,7,8}
##print(set1.issubset(set2))

#3.Find symmetric difference of two sets.

##set1={1,2,3,4,5,6}
##set2={5,6,7,8}
##set3=set1^set2

#4. Count unique elements in a list using a set.

##li=[10,20,30,40,30,10]
##unique_element=set(li)
##count=len(unique_element)
##print(count) 

#5.. Remove all common elements from two sets

##set1={10,30,4,2,41}
##set2={45,4,2,5,11}
##set3=set1^set2
##print(set3)

#                TRICKY

#1. Find missing numbers from 1 to n using sets.

##num=[1,2,5,6]
##n=6
##full_set=set(range(1,n+1))
##given_set=set(num)
##missing_num=full_set-given_set
##print("missing_num",missing_num)

#2. Check if two lists have any common elements.

##li1=[10,20,30,40,50]
##li2=[30,40,50,60,70]
##li3=set(li1)&set(li2)
##print(li3)

#3. Convert a set of strings into uppercase.

##set1={"harsh","rathi","cromacampus","student"}
##set2=set()
##for i in set1:
##    set2.add(i.upper())
##print(set2)

#4. Identify unique vowels in a given string using a set.

##str=input("enter the string:")
##vowel="aeiou"
##
##result=set()
##for ch in str:
##    if ch.lower() in "aeiou":
##        result.add(ch.lower())
##        
##print("unique vowels:",result)



#5.Find elements that appear only once in a list.

##element=[10,50,23,95,21,30,40,23,95]
##element1=set(element)
##print(element1)


###                  DICTIONARY

#Basic 
#1. Create a dictionary and print all keys and values
##
##dict1={"name":"harsh","course":"data science","duration":"9 months"}
##for key,value in dict1.items():
##    print(key,":",value)

#2.Count frequency of each word in a sentence.

##sentence=input("enter the sentence:")
##words=sentence.split()
##freq={}
##for word in words:
##    if word in freq:
##        freq[word]+=1
##    else:
##        freq[word]=1
##    
##print(freq)


#ques3. Merge two dictionaries.

##dict1={"name":"harsh rathi", "course":"data science"}
##dict2={"address":"noida","age":"18"}
##dict3=dict1|dict2
##print(dict3)

#ques4.Find the length of a dictionary. 
##dict1={"name":"harsh rathi", "course":"data science"}
##print(len(dict1))

#ques5. Check if a key exists in a dictionary.]

##dict1={"name":"harsh rathi", "course":"data science"}
##key=input("enter the key:")
##if key in dict1:
##    print("yes exist",key)
##else:
##    print("not exist")

# INTERMEDIATE
#ques6.Sort a dictionary by values.



#ques7.  Find the key with the maximum value.

##dict1={"harsh":65,"ankit":98,"shubam":33}
##max_val=max(dict1, key=dict1.get)
##print(max_val)

#ques 8.  Remove a key from a dictionary.

##dict1={"harsh":65,"ankit":98,"shubam":33}
##rem_key=dict1.pop("harsh")
##print(rem_key)
##print(dict1)

#ques 9.  Convert two lists into a dictionary.

##li1=[1,2,3,4]
##li2=["noida","delhi" ,"gurguram","pune"]
##dict3=dict(zip(li1,li2))
##print(dict3)

#ques10.  Count character frequency using a dictionary.


##str1=input("enter the string:")
##freq={}
##for ch in str1:
##    if ch in freq:
##        freq[ch]+=1
##    else:
##        freq[ch]=1
##print(freq)


#ques 11. Invert a dictionary (swap keys and values).

##def invert_dict(original_dict):
##    inverted={}
##    for key,value in original_dict.items():
##        inverted[value]=key
##    return inverted
##    
##print(invert_dict({"a":1,"b":2,"c":3,"d":4,"e":5}))

#ques 12.  Group elements by frequency using a dictionary.

##def freq_elem(li1):
##    freq={}
##    for x in li1:
##        freq[x]=freq.get(x,0)+1
##    group={}
##    for key,value in freq.items():
##        if value not in group:
##            group[key]=[value]
##        else:
##            group[value].append(key)
##    return group
##print(freq_elem([1,3,4,3,4,4,4,4,4,4,4,4,4,4,1,4,2,1,3,1,1,3]))

#ques 13. Find duplicate values in a dictionary.

##dict1={1:"a",2:"b",3:"a",4:"a",5:"a"}
##freq={}
##for i in dict1.values():
##    freq[i]=freq.get(i,0)+1
##duplicates=[k for k,i in freq.items() if i>1]
##print(duplicates)

#ques 14.   Flatten a nested dictionary.


##dict1 = {
##    "a": 1,
##    "b": {"x": 10, "y": 20}
##}
##flat_dict={}
##for k in dict1:
##    if type(dict1[k])==dict:
##        for sub in dict1[k]:
##            flat_dict[k+"_"+sub]=dict1[k][sub]
##    else:
##        flat_dict[k]=dict1[k]
##print(flat_dict)
