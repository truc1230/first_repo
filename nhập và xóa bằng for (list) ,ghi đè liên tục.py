

studentList = []
studentFile = open ("students1.txt", "r")
for line in studentFile:
    smallList = (line.rstrip()).split()
    studentList.append(smallList)
studentFile.close()
print(studentList)


deleteNumber = input("Enter number: ")
if len(deleteNumber) == 0:
    print("WARNING: Input can not blank -- Please do again!")
    Delete()

while len(deleteNumber) != 2:
    print("Student number must have 8 digits")
    deleteNumber = input("Please try again: ")
    deleteNumber = input("Enter number: ")

for line in studentList:
    if deleteNumber in line:
        studentList.remove(line);
        print("deleted")
print(studentList)
studentFile = open("students1.txt", "w")
for ele in studentList:
    studentFile.write(str(ele) + "\n")
