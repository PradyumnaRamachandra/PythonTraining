
#Linear Search

# alist=[2,3,4,5,6,7,8]
#
# def linear_Search(alist,key):
#     for index,i in enumerate(alist,start=1):
#         if i==key:
#             return index
#     return -1
#
# print(linear_Search(alist,10))


#Prime number Program
# num=11
# if num >1:
#     for i in range(2,num):
#         if num%i==0:
#             print("Not a prime number")
#             break
#     else:
#         print("Number is Prime")
# else:
#     print("Number is not a Prime number")


#Binary search
# def binary_Search(alist,key):
#     start=0
#     end=len(alist)
#
#     while start<end:
#         mid=(start+end)//2
#         if alist[mid]>key:
#             end=mid
#         elif alist[mid]<key:
#             start=mid+1
#         else:
#             return mid
#     return -1
#
# index=binary_Search([2,3,4,5,6],6)
# print(index)

#Bubble Sort
#
# a=[7,1,9,4,6,2,3]
#
# def bubble_sort(alist):
#     n=len(alist)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if alist[j]>alist[j+1]:
#                 alist[j],alist[j+1]=alist[j+1],a[j]
#
#     return alist
#
# print(bubble_sort(a))

#Fibonacci series
#
# a=1
# b=2
# n=10
# while n-2:
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     n=n-1
#
# print(c)

#Number Palindrome

# n=121
# temp=n
# rev=0
# while n>0:
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
#
# print(rev)

# a=1
# print(callable(a))

import timeit
#
# l=[]
# start=timeit.default_timer()
# for i in range(51):
#     l.append(i)
# end=timeit.default_timer()
# print("Time",start-end)
#
#
# t=tuple(range(510))
# start=timeit.default_timer()
# for i in t:
#     # t=t+(i,)
#     print(i)
#
# end=timeit.default_timer()
# print("Time",end-start)


# t=list(range(510))
# start=timeit.default_timer()
# for i in t:
#     print(i)
#
# end=timeit.default_timer()
# print("Time",end-start)
#
# a=[1,2,3,4,5]
# b=(1,2,3,4,5)
# print(a.__sizeof__())
# print(b.__sizeof__())


# Multiple Inheritance
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def showname(self):
#         print(self.name)
#
#     def showage(self):
#         print(self.age)
#
# class Employee():
#     def __init__(self,eid):
#         self.eid=eid
#
#
# class Location(Person,Employee):
#     def __init__(self,name,age,eid,location):
#         Person.__init__(self,name,age)
#         Employee.__init__(self,eid)
#         self.location=location
#
#     def showlocation(self):
#         print(self.location)
#
# e1=Location("Prady",34,82051837,"Bangalore")
# e1.showname()
# e1.showage()
# e1.showlocation()


# class A:
#     def __init__(self):
#         self.name="John"
#         self.age=23
#
# class B:
#     def __init__(self):
#         self.name="Richard"
#         self.age=34
#
# class C(A,B):
#     def __init__(self):
#         B.__init__(self)
#         A.__init__(self)
#
# c1=C()
# print(c1.name)
# #
# class A():
#     def __init__(self):
#         self.name="Prady"
#         self.age=23
#
#     def showname(self):
#         print(self.name)
#
# class B():
#     def __init__(self):
#         self.name="Sandy"
#         self.age=33
#
#       def showname(self):
# #         print(self.name)
#
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#
#     def showname(self):
#         print(self.name)
#
# c1=C()
# c1.showname()
# print(C.mro())
#
# class A():
#     def __init__(self):
#         pass
#
#     def show(self):
#         print("Class A")
#
# class B():
#     def __init__(self):
#         pass
#
#     def show(self):
#         print("Class B")
#
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#
#
# c1=C()
# c1.show()

# Multilevel Inheritance
#
# class Person():
#     def __init__(self):
#         print("Initializing Class Person")
#
#     def showvalue(self,b):
#         print("Printing from class Person",b)
#
# class student(Person):
#     def __init__(self):
#         print("Initializing class student")
#         super().__init__()
#
#     def showvalue(self,b):
#         print("printing from class student",b)
#         super().showvalue(b+1)
#
# class learner(student):
#     def __init__(self):
#         print("Initializing class learner")
#         super().__init__()
#
#     def showvalue(self,b):
#         print("PRinting from class learner",b)
#         super().showvalue(b+1)
#
#
# l=learner()
# l.showvalue(10)
#
# a=[1,2,3,4,5,6,7,8,9]
#
# def binary_search(a,key):
#     start=0
#     end=len(a)
#     while start<end:
#         mid=(start+end)//2
#         if a[mid]>key:
#             end=mid
#         elif a[mid]<key:
#             start=mid+1
#         else:
#             return mid
#     return -1
#
# index=binary_search(a,6)
# print(index)
#
# a=[9,2,5,1,8,7,6]
#
# n=len(a)
# for i in range(n):
#     for j in range(n-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#
# print(a)

# a=1
# b=2
# n=10
# while n-2:
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     n=n-1


