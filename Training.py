#Working with variables

# str="Pradyumna"
# num=25
# num1=35.67
#
#
# str="wwww.apple.com"
#
# num=45
# num1=55.67
#
#
# str="pradyumna"
# str="c"
#
# num=45

# Input and Output
#
# str="Pradyumna"
# print(str)
#
# num=45
# print(num)
#
# num1=45.50
# print(num1)
#
# str="I like to have Coffee"
# print(str)

#Formatting
#
# print(1,2,3,4,5,sep="*")
# #
# # name="Pradyumna"
# # company="DXC"
# #
# # print("My name is {},company is {}".format(name,company))
#
#
# print("My name is {name},and i go to {school}".format(name="Samrudh",school="NPS"))


# # Input
# name=input("Please Enter the name :")
# company=input("Please enter the company :")
# print("My name is{name} and i work in {company}".format(name=name,company=company))

#Working with Operators

# Arithamtic Operators

# x=25
# y=15
#
# print(x+y)
# print(x-y)
# print(x%y)
# print(x//y)
# print(x*y)
# print(x/y)
#
# # Comparison Operators
#
# print(x<y)
# print(x>y)
# print(x==y)
# print(x>=y)
# print(x<=y)
# print(x!=y)
#
# #assignment Operators
# x=1
# y=1
# x=x+1,
# x+=1

# #Logical Operators
#
# x=True
# y=False
#
# print(x and y)
# print(x or y )
# print( not x)

#Identity Opearators
# is , is not

# x=5
# y=10
# print( x is y )
#
# print(id(x))
# print(id(y))

# Membership Operators

# in ,not in

# str="Pradyumna"
#
# print('z' in str)
# print('z' not in str)

# Type Casting
# str="1"
# num=str(str)
#
# print(type(str))
# print(type(num))
#
# num="11"
# num1="25"
#
# result=int(num)+int(num1)
# print(result)

# num=float(input("Enter the First Number :"))
# num1=float(input("Enter the Second Number :"))
#
# result=num+num1
# print(result)

# Strings Functions
#
# str="hello world"
# print(str.capitalize())
#
# print(str.lower())
# print(str.upper())
#
# print(str.count('l'))
# print(str.find('e'))
#
# # print(str[str.find('e'):5])
# print(str.find('l'))
#
# print(str.split(' '))
# print(str.replace("hello","Miss"))
# print(str)
# # print(str1)

# String Slicing

# str="Pradyumna"
#
# print(str[5])
#
# # print(str[start:Stop:step])
# print(str[0:6:2])
#
# print(str[5::-1])
#
# str1=str[-1::-1]
# print(str==str1)

# Conditional Statements

# if <condition>:
#     print("Something")
#
#
# if <condition1>:
#     print("something")
# else:
#     print("Condition 2")
#
#
# if <condition1>:
#     print("Something")
# elif <condition2>:
#     print("Something")
# else:
#     print("Soemthing")

# sex="aaa"
#
# if sex=='m':
#     print("Male Gender")
# elif sex=='f':
#     print("Female Gender")
# else:
#     print("Gender Unknown")
#
#
# #Given number id odd or even
#
# num=float(input("Enter the Number :"))
# if num>0:
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("Enter a number greater than zero")

# List -> Data Structure

# my_list=[1,2,3,4.5,5,6]
# my_list1=["1","2","3","4","5"]
#
# print(my_list)
# print(my_list1)
#
# print(type(my_list))
# print(type(my_list1))

# courses=["Maths","Science","Biology","Botany","Socials"]
# print(courses)
# courses.append("English")
# print(courses)
#
# courses1=["Sanskrit","Hindi"]
# courses.extend(courses1)
# print(courses)
#
# print(courses.index("Biology"))
# courses.insert(2,"Commerce")
# print(courses)
#
# courses.remove("Commerce")
# print(courses)
# # courses.remove(2) # Value Error not in list
#
# popped=courses.pop()
# print(courses)
# print(popped)
#
# # courses.clear()
#
# print(courses)
#
# # str='Hello\'s World'
#
# # Length of the List
# print(len(courses))

# courses=["Maths","Science","Biology","Botany","Socials"]
# courses.sort()
# # print(courses)
# # print(courses)
#
# sort_courses=sorted(courses)
# print(sort_courses)
# print(courses)
#
# courses.sort(reverse=True)
# print(courses)
#
# # del courses
# # sort_courses=sorted(courses,reverse=True)
# print(courses)
#
# num=[9,1,3,5,7,6]
# # num.sort(reverse=True)
# num1=sorted(num,reverse=True)
# print(num1)

# Looping
#
# while (Condition):
#     code

# i=1
# n=25
# while i<=n:
#     print(i)
#     # i=i+1
#     i+=1

# for item in something:
#     code
# for i in range(0,26):
#     print(i)

# for i in range(5,25):
#     print(i)

# for i in range(0,25,2):
#     print(i)

# for i in range(26,1,-1):
#     print(i)

# for i in range(26):
#     if i ==15:
#         continue
#     print(i)

# for i in range(26):
# #     if i ==15:
# #         break
# #     print(i)

# courses=["Maths","Science","Biology","Botany","Socials"]
# for course in courses:
#     print(course)

# for i in a:
#     print(i)
#
# i=1
# n=10
# while i<=n:
#     print(i)
#     i=i+1

# a=[9,5,4,69999999999,2,7,3]
# max_num=a[0]
# for i in a:
#     if i>max_num:
#         max_num=i
#
# print(max_num)

#
# #Linear Search
# a=[3,6,9,899,11,44,77,899,101]
# x=int(input("Enter the number :"))
# # for i in a:
#     if i==x:
#         print(a.index(i))

#enumerate

# for index,i in enumerate(a,start=1):
#     if i==x:
#         print(index)

# length=len(a)
# # for i in range(length):
# #     if a[i]==x:
# #         print(i)


# odd and Even number
#
# odd=[]
# even=[]
# for i in range(51):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# # print("Odd List :"+odd)
# print("Even List :",even)

# a=[9,4,8,3,2,1]
# b=a
# # # b=a.copy()
# # b=a
# # print(id(b))
# # print(id(a))
# b[1]=5
# print(a)
# print(b)

# Working with tuples
#
# my_tuple=(1,2,3,4,5,6,7,8)
# # my_tuple[2]=45
#
# a=1,2,"crew","facet","facet"
# print(a)
#
# # Tuple Unpacking
# b,c,d,e,f=a
# print(b)
# print(c)
# print(d)
# print(e)
#
# # Indexing
#
# print(a.index("crew"))
# print(a.count("facet"))
#
# # Slicing
#
# print(a[0:2])
#
# # iterate over a Tuple
#
# for i in a:
#     print(i)

# b=(1,2,3,[4,5],[6,25])
# b[3][0]=25
# print(b)
# # a=[1,2,3,(4,5)]
# for i in b:
#     if type(i)==list:
#         print(i.index(25))

# To print nested values
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=([1,2,3],[4,5,6],[7,8,9])
#
# for i in a:
#     for j in i:
#         print(j)
#
# for i in b:
#     for j in i:
#         print(j)

# Working with Sets

# a={"PRady","divakar","manoj","magu"}
# b={"sandeep","avinash","mahesh","prashanth"}
# a=list([1,2,3,4])
# b=tuple((1,2,3,4))
# c=set({1,2,3,4})
# a=list([1,2,3,4])
# print(a)
# #
# print(a)
# print(a)
# print(a)
# print(a)
# print(a)
#
# #Adding Elements to set
# a.update({"deepak","kiran"})
# a.update({"mooshandi"})
#
# print(a)
#
#
# # to remove an element from set
# a.remove("mooshandi")
# print(a)
#
# # Pop
# b=a.pop()
# print(b)

# a={"PRady","divakar","manoj","magu"}
# b={"sandeep","avinash","mahesh","prashanth","divakar"}
# # a.add("someting")
#
# union_set=a.union(b)
# print(union_set)
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))

# for item in a:
#     print(item)

# # Set should have only Immutable Elements . It cannot contain "Mutable elements"
# b={1,2,'abc',(4,5,6),[1,2,3]}
# print(b)
#

# city=['Bangalore','Mumbai','Delhi','Chennai']
# str=""
# for i in city :
#     # str=str+" "+i[::-1]
#     # str1="".join(i[::-1])
#     str=str+" "+"".join(i[::-1])
# print(str)
#
# a={"name":"Prady","age":34,"Company":"DXC","EmployeeType":"Regular"}
#
# # print(a)
#
# print(a['name'])
# print(a.get('name'))
#
# a['name']="Divakar"
#
# a['name']="Prady"
# print(a)
#
# a['car']="Honda Amaze"
#
# print(a)
#
# a['Mileage']=27000
#
# print(a)
#
# a.pop('Mileage')
# print(a)
#
# a['Mileage']=27000
# print(a)
# # b=a.popitem()
# # print(b)
# # b=a.popitem()
# # print(a)

# a={"Employee1":{"name":"Prady","age":34,"Company":"DXC","EmployeeType":"Regular"},
#    "Employee2":{"name":"divakar","age":45,"Company":"DXC","EmployeeType":"Regular"}
# }
#
# a['Employee3']={}
# a['Employee3']['name']="Manoj"
# a['Employee3']['age']=35
# a['Employee3']['Company']="DXC"
# a['Employee3']['EmployeeType']="Regular"

# for key in a.keys():
#     print(key)
#
# for values in a.values():
#     print(values)

# for key,value in a.items():
#     print("Key: ",key)
#     for i_key in value:
#         print(i_key+":",value[i_key])


# Working with Dictionary

# my_dict={"name":"Divakar","age":41,"company":"dxc","sex":"Male"}
# print(my_dict["company"])
# print(my_dict["name"])
#
# print(my_dict.get('name'))
#
# my_dict['location']="Bangalore"
#
# print(my_dict)
#
# my_dict.update({"address":"ranebennur","marital Status":"Married"})
#
# print(my_dict)
#
# b={"vehicle":"jupiter"}
#
# my_dict.update(b)
#
# print(my_dict)
#
# del my_dict['vehicle']
# print(my_dict)

# # # Nested Dictionary
# Emp_Details={"Employee1":{"name":"Prady","age":35,"company":"Dxc"},
#              "Employee2":{"name":"manoj","age":35,"company":"Dxc"},
#
#              }
#
# print(Emp_Details)
#
# Emp_Details["Employee3"]={}
# Emp_Details["Employee3"]["name"]="Divakar"
# Emp_Details["Employee3"]["age"]=41
# Emp_Details["Employee3"]["company"]="Dxc"
#
# Emp_Details["Employee4"]={}
# Emp_Details["Employee4"]["name"]="Karthik"
# Emp_Details["Employee4"]["age"]=36
# Emp_Details["Employee4"]["company"]="Dxc"
#
# print(Emp_Details["Employee2"]["name"])

# Loop over Dictionary
#
# # For iterating keys
# for keys in Emp_Details.keys():
#     print(keys)
#
# # For iterating values
#
# for values in Emp_Details.values():
#     print(values)

# for key,value in Emp_Details.items():
#     print(key+":",value)
#
#
# for dic_key,dic_val in Emp_Details.items():
#     print("Key :",key)
#     for key in dic_val:
#         print(key,dic_val[key])

import timeit
#
# lst=[1,2,3,4,5,6,7,8,9]
# start=timeit.default_timer()
# for i in lst:
#     pass
#     # print(i)
# end=timeit.default_timer()
# print("Time",end-start)
#
# tup=(1,2,3,4,5,6,7,8,9)
# start1=timeit.default_timer()
# for i in tup:
#     pass
#     # print(i)
# end1=timeit.default_timer()
# print("Time",end1-start1)


# lst=[1,2,3,4,5,6,7]
# tup=(1,2,3,4,5,6,7)
#
# print(lst.__sizeof__())
# print(tup.__sizeof__())

# Working with functions
#
# def function_name(args):
#    # your code
#    return

# def greet():
#    print("Hi Divakar")
#
#
# greet()
#
# def gree():
#    pass
#
#
# gree()

# def greet(name):
#    print("Hi",name)
#
# greet("Manoj")
# greet("KArthik")

# def get_gender(sex="unknown"):
#    sex=sex.lower()
#    if sex=='m':
#       print("Male")
#    elif sex=='f':
#       print("Female")
#    else:
#       print(sex)
#
# get_gender('m')
# get_gender('f')
# get_gender()
#
# def greet(name,company="DXC"):
#    # print("Hi "+name+",working in "+company)
#       print("Hi {},working in {}".format(name,company))
#
# greet()
#
# Function with *args ( VAriable length arguments )
# def greet(*names):
#    print(type(names))
#    for name in names:
#       print("Hi",name)
#
# # names="Prady","Divakar","Manoj","Karthik"
# greet("Prady","Divakar","Manoj","Karthik")

# def add(*num):
#    sum=0
#    for i in num:
#       sum=sum+i
#    return sum
#
# total=add(1,2,3,4,5,6,7,8,9)
# print(total)

# **kwargs

# def resume(**kwargs):

# def introduction(**data):
#    for key,value in data.items():
#       print(key,value)
#
# introduction(name="Divakar",company="DXC",location="Bangalore",hobbies="PArtying")

# def student(name,age,**marks):
#    print(name)
#    print(age)
#    for subject,mark in marks.items():
#       print(subject+":",mark)
#
# student("PRady",34,english=75,maths=65,social=71,hindi=75)

# d1={1:"name",2:"age"}
# d2={3:"school",4:"result"}
#
# d3={**d1,**d2}
# # d3=d1,d2
# print(d3)

# sentence="look into my eyes and say i love you look into my eyes what are you doing look into my eyes"
# words=sentence.split()
# word_dict={}
# for word in words:
#    word_count=words.count(word)
#    word_dict.update({word:word_count})
#
# print(word_dict)
#
# import time
# import sys
# #
# # str="hello world"
# # for char in str:
# #     print(char,end='')
# #     time.sleep(.25)
#
# str="hello world"
#
# for c in str:
#     sys.stdout.write(c)
#     sys.stdout.flush()
#     time.sleep(.25)

import time
# from Module1.test import add,sub,linear_search


# print(add(5,5))
# print(sub(10,5))
#
#
# lst=[2,3,4,9,1,11,5]
# lst.sort()
# index=linear_search(lst,4)
# if index >0:
#     print("number found in",index)
# else:
#     print("number not found")

# from Module1 import test
#
# print(test.sub(10,5))
# print(test.add(5,5))
# print(test.linear_search([1,2,3,4,5,6],4))

# from Module1.test import *
#
# from Module1.test import add as a
# print(a(5,5))

from Module1.test import add as a
#
# import sys
#
# print(sys.path.append("C:/Users/pr57/Desktop/Selenium_Python"))
#
# print(sys.path)
#
# import Maths as t
# print(t.add(5,5))
#
# # import sys
# # sys.path.append("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files")
# #
# # import PythonModules as PM
# #
# # PM.printforward(10)

## Object Oriented PRogramming

a=10

# each and every thing is treated as object . 10 is a object with a memory location allocated and x is a reference to it

class Person():
    pass


p1=Person()











