"""
	Student API(application program interface)
"""
from Student import * 
from os import system

slist:list = [] 
filename:str = "student.csv" 

def header(message:str)->None:
	system("cls")
	print(message)
	print("---------------------")
	
def checkid(student:Student)->bool:

	for existing_student in slist:
		if existing_student.idno == student.idno:
			return True
	return False

def addStudent() -> None:
    header("Add Student")

    idno = input("Enter IDNO: ")
    lastname = input("Enter LASTNAME: ")
    firstname = input("Enter FIRSTNAME: ")
    course = input("Enter COURSE: ")
    level = input("Enter LEVEL: ")

    student = Student(idno, lastname, firstname, course, level)

    if checkid(student):
        print("Student IDNO already exists!")
    else:
        slist.append(student)
        student_write()
        print("\n")
        print("New Student Added")


def findStudent() -> None:
    header("Find Student")
    idno = input("Enter Student Number to find: ")
    
    for student_found in slist:
        if idno == student_found.idno:
            print("Student Found:")
            print(student_found)
            break
    else:
        print(f"{idno} not found in student list")

def deleteStudent()->None:
    system("cls")
    
    idno = input("Enter Student ID Number to delete: ")
    
    for studentDelete in slist:
        if idno == studentDelete.idno:
            print(f"{idno} found in the list \n {studentDelete}")
            choice = input(f"Do you really want to delete student [{idno}] | Y or N | : ")
            if choice.lower() == "y":
                slist.remove(studentDelete)
                student_write()
                print("Student deleted successfully")
                break
            elif choice.lower() == "n":
                print(f"Student [{idno}] not deleted")
        else:
            print(f"Student Number: {idno} does not exist!!")
    
def updateStudent() -> None:
    system("cls")
    
    idno = input("Enter Student ID Number to update: ")
    
    for studentUpdate in slist:
        if idno == studentUpdate.idno:
            print(f"{idno} found in the list:\n{studentUpdate}")
            
            idno = input("Enter IDNO: ")
            lastname = input("Enter LASTNAME: ")
            firstname = input("Enter FIRSTNAME: ")
            course = input("Enter COURSE: ")
            level = input("Enter LEVEL: ")

            student = Student(idno, lastname, firstname, course, level)

            if checkid(student):
                print("Student IDNO already exists!")
            else:
                slist.remove(studentUpdate)
                slist.append(student)
                student_write()
                print("\n")
                print("Student Updated")
            break
    else:
        print(f"Student Number: {idno} does not exist!!")


def displayAllStudent()->None:
    system("cls")
    f = open(filename)
    slist = f.readlines()
    f.close()
    for s in slist:
	    print(s,end="")
	
def quit()->None:
    system("cls")
    header("Program Terminated")
 
def student_write() -> None:
    with open(filename, "w") as file:
        for student in slist:
            file.write(student.__str__() + "\n")
 
	
