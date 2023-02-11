import csv
students=[]
file_name=open('/home/administrator/ABHIRAM/day3/students.csv','r')

file_stream = csv.reader(file_name)
header = next(file_name)
print(header)
#header = header.repalce('\n','')
header_list = header.split(',')
for row in file_stream:
    obj = {}
    for item in header_list:
        pos =header_list.index(item)
        obj[item]=row[pos]


    students.append(obj)
#print(students)
roll_no=input("Please enter the roll number: ")
found=False
for student in students:
    if student['ROLL NO']==roll_no:
        print("the students details are")
        print("Roll no:%s " % student['ROLL NO'])
        print("Register Number  : %s" % student['REGISTER NO'])
        print("Name  : %s " % student['NAME  '])
        found = True
    if not found:
        print("no such roll number found in the file")