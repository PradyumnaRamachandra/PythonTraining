#
# # Python Introduction
#
# x=10
# y=5
# print("{0}+{1}={2}".format(x,y,x+y))
#
# name="Prady"
# age=34.456
#
# print("Hi %s, Your age is %.2f"%(name,age))
#
# print("1","2","3","5",sep="*")
#
# print("1","2","3","5",end="\n")

# Variable Scope
#
# x="Global X"
#
# def outer():
#     x="Enclosing"
#     def inner():
#         x="Local"
#         print(x)
#
#     inner()
#     print(x)
#
# outer()
# print(x)

# name="**********Prady============="
# print(name.lstrip("*"))
# print(name.rstrip("="))

# name="Miss World"
# print(name.startswith("Miss"))


#Bubble Sort
#
# def bubbleSort(ar):
#    n = len(arr)
#    # Traverse through all array elements
#    for i in range(n):
#    # Last i elements are already in correct position
#    for j in range(0, n-i-1):
#       # Swap if the element found is greater than the next element
#       if ar[j] > ar[j+1] :
#          ar[j], ar[j+1] = ar[j+1], ar[j]
# # Driver code to test above
# ar = ['t','u','t','o','r','i','a','l']


# def binary_search(alist,key):
#     start=0
#     end=len(alist)
#     while start<end:
#         mid=(start+end)//2
#         if alist[mid] > key:
#             end=mid
#         elif alist[mid] < key:
#             start=mid+1
#         else:
#             return mid
#     return -1
#
# index=binary_search([2,3,4,5,6,7,8,9],4)
# print(index)
#
# n=121
# temp=n
# rev=0
# while (n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
#
# print(rev)


# # # Fibonacci series
# a=1
# b=2
# n=10
# while(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     n=n-1
#
# str="PRady"
# # a="".join(reversed(str))
# a=str[3::-1]
# print(a)


#Strings
# my_message='Hello World'
# # print(my_message)
#
# print(len(my_message))
#
# # print(my_message.lower())
# # print(my_message.upper())
#
# # print(my_message.count("Hello"))
# #
# # print(my_message.find('l'))
# #
# # print(my_message[my_message.find('l'):])
#
# new_message=my_message.replace('World','Universe')
# print(new_message)

# greeting='Hello'
# name='Pradyumna'
# print(f'{greeting} {name.upper()}.Welcome !!')
#
# # Integers and FLoats
#
# num=3.76
# print(round(num,1))

# Working with Lists ,Tuple and Sets

# courses=['History','Maths','Science','Social','English','Kannada']
#
# print(courses)
# print(courses[3])
# print(courses[:2])
#
# courses.append('Sanskrit')
# print(courses)
#
# courses.insert(2,'Art')
# print(courses)
#
# courses_2=['Commerce','Hindi']
#
# courses.extend(courses_2)
#
# print(courses)
#
# courses.remove('Hindi')
# print(courses)
# popped=courses.pop()
# print(popped)
#
#
# courses.reverse()
# print(courses)

# nums=[3,6,1,2,4,8,3,9,5]
# # # nums.sort()
# # nums.sort(reverse=True)
# # print(nums)
# #
# # sorted_courses=sorted(courses)
# # print(sorted_courses)
# print(min(nums))
# print(max(nums))
# print(sum(nums))
#
# courses=['History','Maths','Science','Social','English','Kannada']
#
# # print('Kannada' in courses)
#
# # for index,course in enumerate(courses,start=1):
# #     print(index,course)
#
# courses_str=' - '.join(courses)
# print(courses_str)
# courses_str=courses_str.replace(' - '," ")
# print(courses_str)
# new_list=courses_str.split()
# print(new_list)

## Working with Tuples

# tuple1=('History','Maths','Science','Social','English','Kannada')
# tuple2=tuple1
#
# print(tuple2)
#
# print(tuple1.index('Maths'))

## Working with Set

# a={'History','Maths','Science','Social','English','Kannada'}
# print(type(a))
# a.add("Comerce")
# print(a)
# a.remove("Comerce")
# print(a)
# a.pop()
# print(a)
# a.update(a)
# print(a)

# import openpyxl
#
# workbook=openpyxl.load_workbook("C:\\Users\\pr57\\Desktop\\Selenium_Python\\TestObjects.xlsx")
# worksheet=workbook['FormPage']
# rows=worksheet.max_row
# cols=worksheet.max_column
# print(rows)
# print(cols)
# for row in range(2,rows):
#     print(worksheet.cell(row=row,column=1).value)

##Working with dictionary

# student={'name':'Pradyumna','age':34,'courses':['Maths','Science']}
# # print(student)
# # print(student['name'])
# # print(student['courses'])
# # print(student.get('courses'))
# # student.pop('age')
# a=student.popitem()
# # print(student.keys())
# # print(student.values())
# # print(student.items())
# # for key,value in student.items():
# #     print(key,value)
# print(a)
#
# a={1:{'name':'Prady','age':34,'sex':'Male'},2:{'name':'Divakar','age':40,'sex':'Male'}}
#
# # print(a[1]['age'])
#
# a[3]={}
# # print(a)
# a[3]["name"]="Luna"
# a[3]['age']=24
# a[3]['sex']='Female'
# # print(a)
#
# for a_key,a_value in a.items():
#     print("Key is",a_key)
#     for key in a_value:
#         print(key,a_value[key])

# city=['Bangalore','Mumbai','Delhi','Chennai']
# population=[100000,234554,55677544,566864]
#
# print(dict(zip(city,population)))

# line='''look into my eyes and say i like you look into my eyes and say i like you'''
# words=line.split()
# words_count={}
# for word in words:
#     word_count=words.count(word)
#     words_count.update({word:word_count})
#
# print(words_count)

# Working with Conditional Statements

# language="Python"
#
# if language=="Python":
#     print("language is Python")
# elif language=="Java":
#     print("Language is Java")
# elif language=="VB":
#     print("Language is VB")
# else:
#     print("Language is not listed")
#
#
# num=2
# if num>0:
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("Negative number or Number is zero")




# def bubbleSort(ar):
#    n = len(ar)
#    # Traverse through all array elements
#    for i in range(n):
#        # Last i elements are already in correct position
#       for j in range(0, n-i-1):
#           # Swap if the element found is greater than the next element
#           if ar[j] > ar[j+1] :
#               ar[j], ar[j+1] = ar[j+1], ar[j]
# # Driver code to test above
# ar = ['t','u','t','o','r','i','a','l']
# bubbleSort(ar)
# print(ar)

# a=['aba','bcc','323','bcb','abc','a','b','c']
# b=[]
# for i in a:
#     if len(i)>2:
#         if i[0]==i[-1]:
#             b.append(i)
#
# print(b)

####### Working with Loops
# n=10
# i=1
# while i<=n:
#     print(i)
#     i=i+1

#
# i=1
# n=20
# while i<=n:
#     if i==15:
#         break
#     print(i)
#     i=i+1

# for i in range(0,10,2):
#     print(i)
#
# for i in range(10):
#     if i==5:
#         continue
#     print(i)


### Working with Functions

# def greet():
#     print("Welcome to Training")
#
# greet()

# def get_gender(sex='Unknown'):
#     sex=sex.lower()
#     if sex=='m':
#         sex='male'
#     elif sex=='f':
#         sex='female'
#     print(sex)
#
# get_gender('f')

# def greet(*names):
#     for name in names:
#         print("Hi "+name)
#
# greet('Prady','diva','mmmm')

# a=[1,2,3,4,5,6,7,8,9]

# def add_num(*nums):
#     sum=0
#     for num in nums:
#         sum=sum+num
#
#     return sum
#
#
# print(add_num(*a))

# def student(name,age,*marks):
#     print(name)
#     print(age)
#     print(marks)
#
# student("PRady",34,55,66,77,88,99)

# def student(name,age,**marks):
#     print(name)
#     print(age)
#     for subject,mark in marks.items():
#         print(f'{subject}:{mark}')
#
# student("PRady",34,english=55,maths=66,social=77,kannada=88,hindi=99)

# def intro(**data):
#     for key,value in data.items():
#         print(f"{key}:{value}")
#
# intro(firstname="Pradyumna",lastname="Ramachandra",age=33,company="Dxc",hobbies="Travelling")


#### Sorting
#
# a=[-9,-8,-7,6,5,4,3,2,1]
# # a.sort()
# a_sort=sorted(a,key=abs)
# print(a_sort)
#
# class employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#
#     def __repr__(self):
#         return f'{self.name},{self.age},{self.salary}'
#
# e1=employee("Prady",34,8000)
# print(e1)
# e2=employee("Diva",34,3000)
# e3=employee("sandy",34,9000)
#
# employees=[e1,e2,e3]
# print(employees)
#
# def e_sort(emp):
#     return emp.name
#
# s_employees=sorted(employees,key=e_sort)
# print(s_employees)
#
#
# student={'name':'Pradyumna','age':34,'courses':['Maths','Science']}
#
# for key,value in sorted(student.items(),key=lambda x:x[0]):
#     print(key,value)


## Object Oriented Programmming

# Classes and Objects
# import datetime
#
# class Employee():
#
#     #Class Variables
#     num_emps=0
#     raise_amount=1.04
#
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+'.'+last+'@company.com'
#         Employee.num_emps+=1
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay=int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amt(cls,amount):
#         cls.raise_amount=amount
#
#     @classmethod
#     def from_str(cls,emp_str):
#         first, last, pay = emp1_str.split('-')
#         return cls(first,last,pay)
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday()==5 or day.weekday()==6:
#             return False
#         return True
#
# emp1=Employee("Pradyumna","Ramachandra",78000)
# emp2=Employee("Sandhya","Chandrasekhara",98000)
#
# # Employee.set_raise_amt(1.05)
# #
# # print(Employee.raise_amount)
# # print(emp1.raise_amount)
# # print(emp2.raise_amount)
#
# emp1_str="Pradyumna-Ramachandra-50000"
# emp2_str="Sandhya-Chandrasekhara-60000"
#
# # first,last,pay=emp1_str.split('-')
# new_emp1=Employee.from_str(emp1_str)
# print(new_emp1.email)
#
# new_emp2=Employee.from_str(emp2_str)
# print(new_emp2.email)
#
# my_date=datetime.date(2020,5,6)
# print(Employee.is_workday(my_date))

##--------> Inheritance
#
# class Employee():
#
#     #Class Variables
#     raise_amount=1.04
#
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+'.'+last+'@company.com'
#
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay=int(self.pay * self.raise_amount)
#
# class Tester(Employee):
#     raise_amount = 1.10
#
#     def __init__(self,first,last,pay,skill_set):
#         super().__init__(first,last,pay)
#         self.skill_set=skill_set
#
# class Manager(Employee):
#
#     raise_amount = 2.05
#
#     def __init__(self,first,last,pay,employees=None):
#         super().__init__(first,last,pay)
#         if employees is None:
#             self.employess=[]
#         else:
#             self.employees=employees
#
#     def add_emp(self,emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self,emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emp(self):
#         for emp in self.employees:
#             print('--->',emp.fullname())
#
#
# test_1=Tester("Pradyumna","Ramachandra",78000,"Selenium")
# test_2=Tester("Sandhya","Chandrasekhara",98000,"UFT")
# #
# # # print(help(Tester))
# # # print(test_1.pay)
# # # test_1.apply_raise()
# # # print(test_1.pay)
# # # print(Employee.raise_amount)
# #
# # print(test_1.skill_set)
# # print(test_2.skill_set)
#
# manager1=Manager("Kaushik","Ray",5000,[test_1])
# print(manager1.email)
# # manager1.print_emp()
#
# manager1.add_emp(test_2)
# manager1.print_emp()

# Encapsulation
#
# class Car():
#
#     def __init__(self,color,speed):
#         self.__speed=speed
#         self.color=color
#
#     def set_speed(self,value):
#         self.__speed=value
#
#     def get_speed(self):
#         return self.__speed
#
# ford=Car("Red",130)
# # print(ford._Car__speed)
# ford.set_speed(150)
# print(ford.get_speed())
# print(ford._Car__speed)
# Car.__speed=170
# ford.get_speed()

## @property getter and setter
#
# class Employee():
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first,self.last)
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)
#
#     @fullname.setter
#     def fullname(self,name):
#         first, last=name.split(' ')
#         self.first=first
#         self.last=last
#
#     @fullname.deleter
#     def fullname(self):
#         print('Deleting Name !!!')
#         self.first = None
#         self.last = None
#
# emp1=Employee("Pradyumna","Ramachandra",75000)
# print(emp1.email)
# print(emp1.fullname)
#
# emp1.first="Sandy"
# # print(emp1.email)
# # print(emp1.fullname)
# # emp1.fullname="Corey Schafer"
# print(emp1.email)
# # print(emp1.fullname)

### Abstraction
#
# from abc import ABC,abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Square(Shape):
#
#     def __init__(self,side):
#         self.side=side
#
#     def area(self):
#         print(self.side*self.side)
#
#     def perimeter(self):
#         print(self.side*4)
#
# s=Square(4)
# s.area()

## Composition  PArt of Relation
#
# class Salary():
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#
#     def annual_salary(self):
#         print(self.pay*12+self.bonus)
#
# class Employee():
#     def __init__(self,name,age,pay,bonus):
#         self.name=name
#         self.age=age
#         self.obj_salary=Salary(pay,bonus)
#
#     def total_Salary(self):
#         print(self.obj_salary.annual_salary())
#
# e1=Employee("Prady",34,70000,15000)
# e1.total_Salary()

## Aggregation ::  Has a Relationship
#
# class Salary():
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#
#     def annual_salary(self):
#         print(self.pay*12+self.bonus)
#
# class Employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.obj_salary=salary
#
#     def total_salary(self):
#         return self.obj_salary.annual_salary()
#
# salary=Salary(75000,15000)
# emp1=Employee("Prady",34,salary)
# print(emp1.total_salary())

## Exception Handling


from selenium.common.exceptions import *


# str="Pradyumna"
# try:
#     print(str[1])
# except ArithmeticError as e:
#     print("Exception",e)
# except IndexError as e:
#     print(e)
# else:
#     print("No Exception")
# finally:
#     print("Finally block being executed")

# class CoffeeCup():
#     def __init__(self,temperature):
#         self.temperature=temperature
#
#     def drink_coffee(self):
#         if self.temperature>85:
#             raise Exception("Coffee is too hot")
#         elif self.temperature<65:
#             raise Exception("Coffee is too cold")
#         else:
#             print("Enjoy your coffee")
#
# c=CoffeeCup(95)
# c.drink_coffee()

## Working with Text Files
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test.txt","r")as fh:
#    # f_contents=fh.read()
#    f_contents=fh.readlines()
#    for line in f_contents:
#        print(line,end='')

#
# #Memory efficient
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test.txt","r")as fh:
#     size_to_read=10
#     fh_contents=fh.read(size_to_read)
#
#     while len(fh_contents)>0:
#         print(fh_contents,end="")
#         fh_contents = fh.read(size_to_read)

# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test2.txt","w")as fh:
#     for i in range(25):
#         fh.write("This is line%d\n"%(i+1))

### Working with multiple files
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test2.txt","r")as fr:
#     with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test.txt","w")as fw:
#         for line in fr:
#             fw.write(line)

# import json
# # a={
# #     'name':'Prady',
# #     'age':34,
# #     'marks':[45,55,67,88,98],
# #     'pass':'True'
# #   }
# #
# # with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\demo.json","w") as fh:
# #     fh.write(json.dumps(a,indent=2))
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\demo.json","r") as fh:
#    json_value=json.load(fh)
#    for key,value in json_value.items():
#        print(key,value)
#
# with open("C:/Users/pr57/Desktop/SSM/Python/PythonCourse/Files/example_2.json","r")as fh:
#     data=json.load(fh)
#     # for key,value in data['quiz']['sport']['q1'].items():
#     #     print(key+":",value)
#     for key,value in data['quiz']['maths'].items():
#         print(key+"-",value)

# import json
# from urllib.request import urlopen
#
# with urlopen("http://dummy.restapiexample.com/api/v1/employees")as response:
#     source=response.read()
#
# data=json.loads(source)
#
# print(json.dumps(data,indent=2))

# # iterators
# mytuple=('apple','banana','mango','orange')
# myiter=iter(mytuple)
# print(myiter.__next__())
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
#
# mystr="Banana"
# myit=iter(mystr)
#
# print(next(myit))


#iterator class
#
# class mynumbers():
#
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         x=self.a
#         if x<=25:
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
#
# a=mynumbers()
# myiter=iter(a)
#
# for i in myiter:
#     print(i)

# Generators

# def my_function():
#     n=1
#     yield n
#
#     n=n+1
#     yield n
#
#     n=n+1
#     yield n
#
# a=my_function()
#
# print(next(a))
# str="banana"
# for i in str:
#     print(i)
#
# print(next(a))

# def my_function():
#     for i in range(5):
#         yield i
#
# a=my_function()
# for i in a:
#     print(i)

# a=[3,4,10]
# generator=( x**2 for x in a)
# print(generator)
# print(next(generator))
# print(next(generator))


#Lambda

# def double(x):
#     return x*2
#
# def add(x,y):
#     return x+y
#
# a=double(2)
# print(a)
#
# double=lambda x:x*2
# print(double(2))
#
# add=lambda x,y:x+y
# print(add(4,5))

# #Map function
#
# def length(n):
#     return len(n)
#
# a=map(length,['apple','banana'])
# print(list(a))
# list1=[1,2]
# list2=[3,4]
# b=map(lambda x,y:x+y,list1,list2)
# print(tuple(b))

#Closures

# def outer_func():
#     message="Hi"
#     def inner_func():
#         print(message)
#     return inner_func
#
# myfunc=outer_func()
# myfunc()
#
# def outerfunc(msg):
#     def innerfunc():
#         print(msg)
#     return innerfunc
#
# hi_func=outerfunc("Hi")
# hello_func=outerfunc("Hello")
#
# hi_func()
# hello_func()

# def wrapperfunc(func):
#     def innerfunc(*args):
#         print(func(*args))
#     return innerfunc
#
# def add(x,y):
#     return x+y
#
# adder_func=wrapperfunc(add)
# adder_func(5,6)

# Decorators
#
# def decorator_func(func):
#     def wrapper_func(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper_func
#
# @decorator_func
# def display():
#     print("display function ran")
#
# @decorator_func
# def display_info(name,age):
#     print("display info ran with {},{}".format(name,age))

# decorated_display=decorator_func(display)
# decorated_display()

#
# display()
# display_info("Prady",34)

#
# class decorator_class():
#
#     def __init__(self,original_func):
#         self.original_func=original_func
#
#     def __call__(self, *args, **kwargs):
#         print("call method is being executed")
#         return self.original_func(*args,**kwargs)
#
#
#
# @decorator_class
# def display():
#     print("display function ran")
#
# @decorator_class
# def display_info(name,age):
#     print("display info ran with {},{}".format(name,age))
#
#
# display()
# display_info("Prady",34)

#
# def decorator_func(func):
#     def wrapper_func(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper_func
#
# @decorator_func
# def display():
#     print("display function ran")
#
# @decorator_func
# def display_info(name,age):
#     print("display info ran with {},{}".format(name,age))
#
# decorated_display=decorator_func(display)
# decorated_display()
#
#
# display()
# display_info("Prady",34)

# List Comprehensions

# my_list=[i for i in range(11)]
# print(my_list)
#
# my_list1=[i*i for i in range(10)]
# print(my_list1)

# my_list=[i for i in range(25) if i%2==0]
# print(my_list)

# mylist=[]
# for letter in 'abcd':
#     for num in range(4):
#         mylist.append((letter,num))
#
# print(mylist)
#
# mylist=[(letter,num)for letter in 'abcd' for num in range(4)]
# print(mylist)


## Dictionary Comprehensions

# names=['bruce','clark','peter','Logan','Wade']
# hero=['batman','Superman','Spiderman','Wolverine','DeadPool']
#
# # mydict={}
# # for name,hero in zip(names,hero):
# #     # mydict.update({name:hero})
# #     mydict[name]=hero
# #
# # print(mydict)
#
# my_dict={name:hero for name,hero in zip(names,hero) if name!='peter'}
# print(my_dict)


