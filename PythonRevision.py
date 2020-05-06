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

class Employee():

    #Class Variables
    raise_amount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'


    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

class Tester(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,skill_set):
        super().__init__(first,last,pay)
        self.skill_set=skill_set

class Manager(Employee):

    raise_amount = 2.05

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employess=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())


test_1=Tester("Pradyumna","Ramachandra",78000,"Selenium")
test_2=Tester("Sandhya","Chandrasekhara",98000,"UFT")
#
# # print(help(Tester))
# # print(test_1.pay)
# # test_1.apply_raise()
# # print(test_1.pay)
# # print(Employee.raise_amount)
#
# print(test_1.skill_set)
# print(test_2.skill_set)

manager1=Manager("Kaushik","Ray",5000,[test_1])
print(manager1.email)
# manager1.print_emp()

manager1.add_emp(test_2)
manager1.print_emp()

