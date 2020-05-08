
#Linear Search

# alist=[2,3,4,5,6,7,8]
#
# def linear_Search(alist,key):
#     for index,i in enumerate(alist):
#         if i==key:
#             return i
#     return -1
#
# print(linear_Search(alist,10))

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