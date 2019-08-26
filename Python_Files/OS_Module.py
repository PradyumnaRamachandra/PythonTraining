import os

#print(os.getcwd())
os.chdir("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files")
# print(os.getcwd())
# os.mkdir()
#os.makedirs("OS-Demo\\sub-dir")
# fh=open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files\\log1.txt","w")
# print(os.listdir())
# counter=0
# dir_list=os.listdir()
# count=len(dir_list)
# for i in range(count):
#     if ".txt" in dir_list[i]:
#         print("yes")
#         counter=counter+1
#         #fh.write(dir_list[i])
#         fh.write(dir_list[i]+"\n")
#
# print(counter)
#
# fh.close()

# for dirpath,dirname,files in os.walk("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files"):
#     print(dirpath)
#     print(dirname)
#     print(files)

# print(os.environ.get("HOME"))
#print(os.path.dirname("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files"))
print(os.path.exists("C:\\Users\\pr57\\Desktop\\SSM\\Python\\PythonCourse\\Files"))