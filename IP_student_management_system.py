
import json

FILE = "students.json"


# Load file

def loadFile():
    try:
        with open (FILE, "r") as file:
            return json.load(file)
    except:
        return []
    


# Save file

def saveFile(students):
    with open(FILE, "w") as file:
        json.dump(students, file, indent = 4)



# Add student

def addStudent(students):
    sid = input("Enter ID : ")

    for i in students:
        if i["id"] == sid:
            print("ID already exist")
            return

    name = input("Enter name : ")
    grade = input("Enter grade : ")

    students.append({
        "id" : sid,
        "name" : name,
        "grade" : grade
    })    

    saveFile(students)
    print("\nStudent added successfully!")


# View Student

def viewStudent(students):
    if not students:
        print("Student not found")
        return
    
    print("\n----------- Student List -----------")

    for i in students:
          print("ID:", i["id"], "| Name:", i["name"], "| Grade:", i["grade"])



# Delete student

def deleteStudent(students):
    sid = input("Enter student ID to delete : ")

    for i in students:
        if i["id"] == sid:
            students.remove(i)
            saveFile(students)
            print("Deleted successfully")

            return
        
    print("Student not found")





# main function
students = loadFile()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit\n")

    choice = input("Enter choice: ")

    if choice == "1":
        addStudent(students)
    elif choice == "2":
        viewStudent(students)
    elif choice == "3":
        deleteStudent(students)
    elif choice == "4":
        print("--------> Program teminated <--------")
        break
    else:
        print("Invalid choice")


