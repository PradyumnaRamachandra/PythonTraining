# counter=0
# line_lst=[]
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r") as fh:
#     content=fh.readlines()
#     # print(content,end="")
#     for line in content:
#         # print(line,end="")
#         if "Red" in line:
#             a=line.replace("Red","Green")
#             counter=counter+1
#             line_lst.append(a)
#
#
#
# print(line_lst)
# print("No of times the word was replaced is",counter)
#
# counter=0
# line_lst=[]
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt","r") as fh:
#     content=fh.readlines()
#     count=len(content)
#     # print(count)
#     for i in range(count):
#         if "Red" in content[i]:
#             a=content[i].replace("Red","Green")
#             counter=counter+1
#         line_lst.insert(i,a)
#
# print(line_lst)
# print("No of times the word was replaced is",counter)


# Fibonacci series
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# n=int(input("Enter the series"))
# while(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     n=n-1

a=[2,8,7,4,5,22,99,12,13]
print(type(a))
def func_sort(lst):
    if type(lst)==list:
        sorted_lst=sorted(lst)
        return sorted_lst

print(func_sort(a))

