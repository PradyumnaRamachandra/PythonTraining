
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



#
# n=5
#
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


#
# n=5
# k=2*n-2
# for i in range(0,n):
#
#     for j in range(0,k):
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+1):
#         print("* ",end="")
#     print()

# #
#
# n=5
# num=1
# for i in range(1,n+1):
#     num=1
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+1
#     print()

#
# a=[1,2,3,4,5,6,7,8]
# key=2
# start=0
# end=len(a)
# flag=""
# while start<end:
#     mid=(start+end)//2
#     if a[mid]>key:
#         end=mid
#     elif a[mid]<key:
#         start=mid+1
#     else:
#         print(mid)
#         flag="found"
#         break
#
# if flag=="":
#     print("element not found ")
#

#
#
# def sorted_list(lst):
#     return lst[1]
#
#
# print(sorted(x,key=sorted_list))

#
# a = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
#
# # def func(x):
# #     print(x)
# #
# # func(a)
#
# sorted_a=sorted(a)
# print(sorted_a)
#
# x = [('Bangalore', 25,9), ('Delhi', 35,7), ('Chennai', 37,5), ('Mumbai', 32,1)]
#
# def a(x):
#     return x[2]
# print(sorted(x,key=a))

# a = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
# def b(x):
#     return x[1]
#
# print(sorted(a.items(),key=b))
#
# prices = {
#         'ACME': 45.23,
#         'AAPL': 612.78,
#         'IBM': 205.55,
#         'HPQ': 37.20,
#         'FB': 10.75
#         }
#
# # a,*_,b=(sorted(prices.items(),key=lambda x:x[0]))
# # print(a,*_,b)
#
# print(sorted(prices.items(),key=lambda x:x[1]))
# print(sorted(prices.items(),key=lambda x:x[-1]))
# a=[["fname","lastname"],['mary','lamb']]
#
# print(sorted(a,key=lambda x:x[1][::-1]))

# a=[1,4,3,7,67,[88,99]]
# new_list=[]
# def max_list(x):
#     for i in x:
#         if type(i)==list:
#             max_list(i)
#         else:
#             new_list.append(i)
#     return max(new_list)
#
# print(max_list(a))