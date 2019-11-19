#
# # # To check if Particular Windows Service is Running
# #
# # import psutil
# #
# # # name="AppMgmt"
# # # service=psutil.win_service_get(name)
# # # service=service.as_dict()
# # # print(service)
# #
# #
# #
# # def getService(name):
# #
# #     service = None
# #     try:
# #         service = psutil.win_service_get(name)
# #         service = service.as_dict()
# #     except Exception as ex:
# #         print(str(ex))
# #     return service
# #
# # service = getService('Dhcp')
# # print(service)
# #
# # if service:
# #     print("service found")
# # else:
# #     print("service not found")
# #
# #
# # if service and service['status'] == 'running':
# #     print("service is running")
# # else:
# #     print("service is not running")
#
# #
# # a='pradyumna'
# # print(a)
# #
# # a,b,c=13,"man",5.2
# # print(a)
# # print(b)
# # print(c)
# #
# # from Basics import Constants
# # print(Constants.Name)
# # print(Constants.Company)
# #
# # import sys
# #
# # print(sys.path)
# #
# # sys.path.append("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse")
# #
# # import Constants
# #
# # print(sys.path)
# # print(Constants.Name)
#
# #
# # name="Pradyumna"
# # print("The name is "+name)
# #
# # num=45
# # num1="55"
# #
# # # Type Casting
# # print(num+int(num1))
# #
# # #Formatting
# #
# # print(1,2,3,4,5,end="*")
# # print("\n")
# # print(2,3,4,5,6,sep="*")
#
# #
# # x=10
# # y=15
# #
# # print("{0}+{1}={2}".format(x,y,x+y))
# #
# # name="Pradyumna"
# # age=34.543
# #
# # print("Hi %s,Your age is %.2f"%(name,age))
#
#
# # global a
# # a=10
# # def outerfunc():
# #     a=5
# #     print(a)
# #     def innerfunc():
# #         a=20
# #         print(a)
# #
# #     innerfunc()
# #     print(a)
# #
# #
# # print(a)
# # outerfunc()
# # print(a)
#
# # x=5
# # y=10
# #
# # print(x+y)
# # print(x-y)
# # print(x*y)
# # print(x/y)
# # print(x**y)
#
# # x="Hello World"
# # print("e" in x)
# #
# # x=10
# # y=5
# #
# # print(x is not y)
#
# # x="python training"
# # print(x.capitalize())
# #
# #
# # print(x.upper())
# # print(x.lower())
# # print(x.isupper())
# # print(x.islower())
#
#
# # x="Python Training is fun"
# # # y=x.replace("fun","boring")
# # # print(y)
# #
# # y=x.split(" ")
# # for i in y:
# #     print(i)
#
# # x="madam"
# # y="".join(reversed(x))
# # print(y)
#
# # y=x[::-1]
# # print(y)
# # if x==y:
# #     print("True")
#
# # x="Prady "
# # print(x*100,sep="*")
# #
# # name=input("Enter the name :")
# # if name=="Pradyumna":
# #     print("Company is DXC")
# # elif name=="Sandeep":
# #     print("Company is Benz")
# # elif name=="Divakar":
# #     print("Company is DXC")
# # else:
# #     print("Company not listed")
# #
# #
# # a=[[1,2,3,4,5,6,7],[8,9,10,11,12,13]]
# # for i in a:
# #     for x in i:
# #         print(x)
#
# #
# # a=[]
# # print(a)
# #
# # a=[1,2,3,4,5,65,43,23,45,67]
# # print(a)
# # b=[1,2,3,4,5,65,43,23,45,67]
# #
# #
# # print(a[4])
# #
# # c="Pradyumna"
# # print(c[2:5])
#
# a=[1,2,3,4,5,65,43,23,45,67]
#
# # print(a[::-1])
# #
# # b=[[1,3,4,5,3,6,7],[3,6,4,3,8,9]]
# #
# # print(b[0][4])
#
#
# #
# # odd[0]=1
# # print(odd)
# #
# # odd[1:4]=3,5,7
# # print(odd)
#
# # odd1=[3,4,5,6]
#
# # c=odd+odd1
# # print(c)
# # odd2=odd
# # print(odd2)
#
# # odd.insert(1,3)
# #
# # print(odd)
# #
# # odd.extend([4,5,6,7,8,9])
# # print(odd)
# #
# # odd.append(2)
# # print(odd)
# #
# # odd.remove(7)
# # print(odd)
# #
# # del odd[7]
# # print(odd)
#
#
#
#
#
# #
# odd=[2,4,6,8]
# #
# # odd.pop(1)
# # print(odd)
# # odd.pop()
# # print(odd)
#
# for i in range(5):
#     odd.append(i)
#
# print(odd)

#
# a=[1,3,5,6,7,8]
# b=a.copy()
#
# print(b)
#
# b[1]=34
# print(a)
# print(b)
#
#
# # b.sort(reverse=True)
# # print(b)
#
# b.reverse()
# print(b)
#
# print(sorted(a))
a=[[1,2,3,4,5,6,7],[8,9,10,11,12,13]]

# for i in a:
#     print("first list",i)
#     for x in i:
#         print(x)

# import os
#
# print(os.getcwd())
# dir_list=os.listdir(os.getcwd())
# print(dir_list)
# count=len(dir_list)
#
# for i in dir_list:
#     print(i)
#
# a=[12,2,3,55,66,34,76,456,56]
#
# # a.sort()
# # print(a)
# # max=a[0]
# # for i in a:
# #     if i>max:
# #         max=i
# # print(max)
#
# def sorted_function(lst):
#     if type(lst)==list:
#         lstsort=sorted(lst)
#         # print(lstsort)
#     return lstsort
#
# print(sorted_function(a))

#
# print(a)
# print(type(a))
#
# a=1,2,3,'abc','bcd'
# print(a)
#
# a,b,c,d,e=a
# print(b)
# print(c)
#
# a=("abc")
# print(type(a))
#
# a=("abc",)
# print(a)

# a=(1,2,3,[4,5])
# # print(a[0])
# #
# # print(a[:])
# #
# # a[2]=7
# # print(a)
# a[3][1]=7
# print(a)
#
# print(a.count(2))
#
# for i in a:
#     print(i)

#
# b=((1,2,3),(4,5,6),'abc','def',(7,8,9))
#
# for i in b:
#     for x in i:
#         print(x)


# a={1,2,3,4,5,'abc'}
# print(a)
#
# print(type(a))
#
# a={1,2,'abc',(1,2),[2,3]}
# print

# a={}
#
#
# a=set()
# print(type(a))
#
# a={1,2,3,4,5,6,7}
#
# # print(a[1])
#
# a.add(99)
# print(a)
#
# a.update({8,66,77,88})
# print(a)
#
# a.update([33,44])
# a.discard(33)
# print(a)
# a.remove(44)
# print(a)
#
# for i in a:

#     print(i)
#
# a=sorted(a)
# print(a)
#
# a.sort(key=)
# print(a)
#
# def takesecond(lst):
#     return lst[1]
#
#
#
# a=[(4,5),(2,3),(8,9)]
#
# a.sort(key=takesecond)
# print(a)

# a={1,2,3,4,5}
# print(a.pop())
# print(a.pop())
# print(a.pop())


# city=['Bangalore','Chennai','Pune','Bhubaneshwar','Indore']
# population=[2000000,1500000,2300000,100000,3000000,4000000]
# #
# for index, item in enumerate(city,start=1):    # enumerate returns a tuple of index, item pair
#     print(index, item)
# #
# # a=[]
# # for i in zip(city,population):
# #     a.append(i)
# #
# # print(a)
#
# a=['asdas','adasd','asdasd','sadfs']
#
# for index,i in enumerate(a,start=1):
#     print(index,i)
# a=['milk','bread','butter']
# # enuma=enumerate(a)
# # print(list(enuma))
#
# for index,item in enumerate(a,start=1):
#     print(index,item)

# a={}
# print(type(a))
#
# a={
#     1:'apple',
#     2:'mango',
#     3:'grapes'
# }

# print(a)
#
# print(a[1])
# print(a.get(3))
#
# car={
#     'make':'Honda',
#     'colour':'Maroon',
#     'model':'2017'
# }
#
# car['model']=2016
#
# print(car)
#
# car['mileage']=25000
#
# print(car)
#
# car['service']='Trident'
#
# print(car)
#
# car.pop('service')
# print(car)
# car.popitem()
# print(car)
#
# car['mileage']=25000
# print(car)
#
# car.update({'model':'bus'})
#
# print(car)
#
# for i in car:
#     print(i)
#
# for i in car.values():
#     print(i)
#
# for key,value in car.items():
#     print(key,":",value)
#
# car.update({'model':'Amaze'})
#
# for key,value in car.items():
#     print(key, ":",value)

#
# a={1:{'name':'Prady','age':34,'sex':'Male'},2:{'name':'Divakar','age':40,'sex':'Male'}}
#
# print(a[2]['sex'])
#
# a[3]={}
# a[3]['name']='sandeep'
# a[3]['age']=38
# a[3]['sex']='male'
#
# print(a)
# print(a[3]['sex'])
#
#
# for key,value in a.items():
#     print("Dict",key)
#     for x in value:
#         print(x,":",value[x])



#
# line="look into my eyes and say i like you look into my eyes and say i like you"
# words=line.split()
# print(words)
# count_dic={}
# for i in words:
#     count=words.count(i)
#     count_dic.update({i:count})
#
# print(count_dic)

# n=20
# i=1
# while i<=n:
#     print(i)
#     i=i+1
#
# sum=0
# for i in range(51):
#     sum=sum+i
#
# print(sum)



# def get_gender(sex='unknown'):
#     sex=sex.lower()
#     if sex=='m':
#         print("Male")
#     elif sex=='f':
#         print("Female")
#
#
# get_gender()

# def greet_names(*names):
#     for i in names:
#         print("Hello",i)
#
# greet_names("PRady","Diva","sandeep","sandy","guttalu")

# def student(name,age,*marks):
# #     print("Name is ",name)
# #     print("Age is ",age)
# #     print("Marks is ",*marks)
# #
# # student("PRady",35,45,55,66,77,88)

# def student(name,age,**marks):
#     print("Name is ", name)
#     print("Age is ",age)
#     for subject,value in marks.items():
#         print(subject,":",value)
#
# student("Prady",35,maths=45,english=75,kannada=86,social=56)
#
# def intro(**data):
#     for key,value in data.items():
#         print(key,"is",value)
#
# intro(firstname="Prady",lastname="Ramachandra",age=35,company="DXC")

# class Employee():
#
#     emp_count=0
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Employee.emp_count=Employee.emp_count+1
#
#     def show_name(self):
#         print("Name is",self.name)
#
#     def show_age(self):
#         print("Age is ",self.age)
#
#     def employee_count(self):
#         print("Employee count is ",Employee.emp_count)
#
#
# e1=Employee("Prady",35)
# e1.show_name()
# e1.show_age()
# e2=Employee("Diva",40)
# e2.show_name()
# e2.show_age()
# e2.employee_count()
#
# e1.age=45
#
# e1.show_age()
# e2.show_age()
#
# class Person():
#     def __init__(self,fname,lastname):
#         self.fname=fname
#         self.lastname=lastname
#
#     def print_name(self):
#         print(self.fname,self.lastname)
#
#
# class student(Person):
#     pass
#
#
# s1=student("Prady","Ramachandra")
# s1.print_name()

# class Polygon():
#     height=None
#     width=None
#
#     def set_values(self,height,width):
#         self.height=height
#         self.width=width
#
#
# class Rectangle(Polygon):
#     def area(self):
#         print("Area of Rectangle is ",self.height *self.width)
#
#
# class Triangle(Polygon):
#     def area(self):
#         print("Area of Triange is ",self.height*self.width/2)
#
#
#
# r1=Rectangle()
# r1.set_values(35,45)
# r1.area()
#
# tri=Triangle()
# tri.set_values(44,55)
# tri.area()

# class person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
#     def print_name(self):
#         print(self.name,self.age)
#
# class student():
#
#     def __init__(self,id):
#         self.id=id
#
#     def show_id(self):
#         print(self.id)
#
#
# class Address(person,student):
#     def __init__(self,name,age,id,location):
#         person.__init__(self,name,age)
#         student.__init__(self,id)
#         self.location=location
#
#
#     def show_location(self):
#         print(self.location)
#
# a1=Address("PRady",35,5555,"Blore")
# a1.print_name()
# a1.show_id()
# a1.show_location()
# print(Address.__mro__)
#
# num1=float(input("Enter the first number :"))
# num2=float(input("Enter the second number :"))
# result=None
# try:
#     result=num1/num2
# except Exception as e:
#     print("The Exception is ",e)
#
# else:
#     print("There was no Exception")
# finally:
#     print("Finally block is being executed")
#
# class coffee():
#     def __init__(self,temperature):
#         self.temperature=temperature
#
#     def drink_coffee(self):
#         if self.temperature>=75:
#             raise Exception("Coffee is too hot")
#         elif self.temperature<60:
#             raise Exception("Coffee is too cold")
#         else:
#             print("Enjoy your coffee . A lot can happen over coffee")
#
# c1=coffee(70)
# c1.drink_coffee()

# try:
#     with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log.txt",'r')as fh:
#         text=fh.readlines()
#         print(text)
#
# except Exception as e:
#     print("Exception is ",e)
#
#
# mylist=['Apple','Banana','Cherry']
# it=iter(mylist)
# print(it.__next__())
# print(next(it))
# print(next(it))
# print(next(it))

# class MyNumbers():
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         x=self.a
#         if self.a<=25:
#             self.a=self.a+1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass=MyNumbers()
# myiter=iter(myclass)
#
# for i in myiter:
#     print(i)

# def myfunc():
#     for i in range(25):
#         yield i
#
# a=myfunc()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# def double(x):
#     return x*2
#
# def add(x,y):
#     return x+y
#
# def product(x,y,z):
#     return x*y*z
#
#
# print(double(2))
# print(add(5,4))
# print(product(5,6,7))
#
# double=lambda x:x*2
# print(double(4))
#
# add=lambda x,y:x+y
# print(add(5,4))
#
# product=lambda x,y,z:x*y*z
# print(product(5,6,7))

#
# mylist=[2,4,6,8,9,3,5]
# mylist1=[5,4,6,7]
#
# # # result=map(add,mylist,mylist1)
# # # print(list(result))
# #
# # def func(x):
# #     if x%2==0:
# #         return x
# #
# # result=filter(func,mylist)
# # print(list(result))
#
#
# from functools import reduce
# d=reduce(lambda x,y:x+y,mylist)
# print(d)

# class car():
#
#     def __init__(self,name,colour):
#         self.name=name
#         self.__colour=colour
#         print(self.__showowner())
#
#     def setspeed(self,value):
#         self.__colour=value
#
#     def getspeed(self):
#         return self.__colour
#
#     def __showowner(self):
#         print("Owner name is private")
#
# ford=car("ecosport","Red")
#
# ford.setspeed("Green")
# print(ford.getspeed())
# ford._car__colour="White"
# print(ford.getspeed())

from abc import ABC,abstractmethod

# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):pass
#
#     @abstractmethod
#     def perimeter(self):pass
#
# class Square(Shape):
#
#     def __init__(self,side):
#         self.side=side
#
#     def area(self):
#         print("Area of a square is ",self.side*self.side)
#
#     def perimeter(self):
#         print("Perimeter of Square is",self.side*4)
#
# s1=Square(8)
# s1.area()
# s1.perimeter()
#
# class Salary():
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#
#     def annual_salary(self):
#         return self.pay*12+self.bonus
#
# class Employee():
#     def __init__(self,name,age,pay,bonus):
#         self.name=name
#         self.age=age
#         self.obj_salary=Salary(pay,bonus)
#
#     def total_Salary(self):
#         return self.obj_salary.annual_salary()
#
# e1=Employee("Prady",35,70000,25000)
# print(e1.total_Salary())

#
# class Salary():
#     def __init__(self,pay,bonus):
#         self.pay=pay
#         self.bonus=bonus
#
#     def annual_salary(self):
#         return self.pay*12+self.bonus
#
# class Employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.obj_salary=salary
#
#     def Total_Salary(self):
#         return self.obj_salary.annual_salary()
#
# salary=Salary(750000,25000)
# e1=Employee("Prady",35,salary)
# print(e1.Total_Salary())

# a=["1","2","3","4","5","6","7","89"]
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test.txt",'w') as fh:
#     for i in a:
#         fh.write(i+"\n")

# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test.txt",'w') as fh:
#     for i in range(15):
#         fh.write("Welcome to Python %d\n"%(i+1))
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test.txt",'r') as fh:
#     text=fh.readlines()
#     for i in text:
#         print(i)
#
import json
#
# a={
#     'name':'Pradyumna',
#     'age':35,
#     'marks':[45,66,44,34,78],
#     'result':'Pass'
# }
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test_json.json",'w') as fh:
#     fh.write(json.dumps(a,indent=2))
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\test_json.json",'r') as fh:
#     json_value=json.load(fh)
#     for key,value in json_value.items():
#         print(key,value)

# def outerfunc(text):
#     def innerfunc():
#         print(text)
#     return innerfunc
#
# a=outerfunc("Hello")
# ##del outerfunc
# a()


# str="werwerwerwer"
#
# lst=[i for i in str]
# print(lst)
#
# import xlrd
#
# file="C:\\Users\\pr57\\Desktop\\SSM\\Python\\data.xlsx"
# workbook=xlrd.open_workbook(file)
# sheet=workbook.sheet_by_index(0)
# print(sheet.ncols)
#
# for col in range(sheet.ncols):
#     print(sheet.cell_value(1,col))
#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# import time
#
# driver=webdriver.Chrome(executable_path="C:\\PythonProjects\\Python_Selenium\\drivers\\chromedriver.exe")
# driver.maximize_window()
# driver.get("https://learn.letskodeit.com/p/practice")
#
# wait=WebDriverWait(driver,40,poll_frequency=1)
# element=wait.until(ec.element_to_be_clickable(("xpath","//input[@type='radio']")))

####################################################################
# elements=driver.find_elements_by_xpath("//input[@type='radio']")
# for element in elements:
#     if element.is_selected()==False:
#         element.click()
# #driver.find_element_by_xpath("//input[@id='bmwradio']").click()
#
# drop_item=driver.find_element_by_xpath("//select[@id='carselect']")
# sel=Select(drop_item)
# sel.select_by_value("honda")
#
# driver.find_element_by_xpath("//button[@id='openwindow']").click()
#
# parentwindow=driver.current_window_handle
#
# handles=driver.window_handles
# for i in handles:
#     if i not in parentwindow:
#         driver.switch_to.window(i)
#         wait=WebDriverWait(driver,30,poll_frequency=1)
#         element=wait.until(ec.element_to_be_clickable(("xpath","//input[@id='search-courses']")))
#         driver.find_element_by_xpath("//input[@id='search-courses']").send_keys("Python")
#         time.sleep(2)
#         driver.close()
#         break
#
# driver.switch_to.window(parentwindow)
# driver.find_element_by_xpath("//input[@id='name']").send_keys("Pradyumna")
# driver.find_element_by_xpath("//input[@id='alertbtn']").click()
# time.sleep(1)
# alert=driver.switch_to.alert
# alert.accept()
#
# elem=driver.find_element_by_xpath("//table[@id='product']/tbody/tr[3]/td[2]")
# print(elem.text)

####################################################################################
#
# driver.execute_script("window.scrollBy(0,500);")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,-500);")
# time.sleep(2)
#
# element=driver.find_element_by_xpath("//legend[contains(text(),'Mouse')]")
#
# driver.execute_script("arguments[0].scrollIntoView(true);",element)
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,-100);")
#
# from selenium.webdriver import ActionChains
# action=ActionChains(driver)
# mousehover=driver.find_element_by_xpath("//button[@id='mousehover']")
# action.move_to_element(mousehover).perform()
# eletop=driver.find_element_by_xpath("//a[contains(text(),'Top')]")
# action.move_to_element(eletop).click().perform()
# from selenium.webdriver.common.keys import Keys
#
# element=driver.find_element_by_xpath("//iframe[@id='courses-iframe']")
# driver.execute_script("arguments[0].scrollIntoView(true);",element)
# time.sleep(2)
# driver.switch_to.frame("iframe-name")
# driver.find_element_by_xpath("//input[@id='search-courses']").send_keys("Python")
# driver.find_element_by_xpath("//input[@id='search-courses']").send_keys(Keys.RETURN)
# time.sleep(3)
# driver.switch_to.default_content()
# driver.close()
#

