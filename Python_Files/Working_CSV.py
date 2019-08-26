import csv

# row=list(csv_reader)
# print(row)
# next(csv_reader)

with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\UsersSample.csv","r")as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        print(line)
#
#     with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\new_file.csv","w")as new_file:
#         csv_writer=csv.writer(new_file)
#
#         for row in csv_reader:
#             csv_writer.writerow(row)
#
# with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\UsersSample.csv","r")as csv_file:
#     csv_reader=csv.DictReader(csv_file)
#
#     with open("C:\\Users\\pr57\\Desktop\\SSM\\Python\\new_file.csv", "w")as new_file:
#         fieldnames=['FIRST NAME ','LAST NAME','USERNAME ','PASSWORD ','EMAIL ADDRESS','PHONE NUMBER','PASSPORT','GROUPS','USERCODE','TITLE','ADDRESS 1 ','ADDRESS 2','CITY','STATE','ZIP']
#         csv_writer=csv.DictWriter(new_file,fieldnames=fieldnames)
#
#         for line in csv_reader:
#                 csv_writer.writerow(line)


