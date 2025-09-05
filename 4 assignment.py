# SRMs

records=[]

def add():
    name=input("Enetr student name :")
    roll=input("Enetr student roll no. :")
    course=input("Enetr student course :")
    marks=input("Enetr student marks :")

    student={
        "Name" : name,
        "Roll no" : roll,
        "Course" : course,
        "Marks" : marks,
        }
    
    records.append(student)
    print("========================")
    print("Record added succefully ")

    

def dis():
    if records:
         print("Students records")
         print("------------------")
         for record in records:
             print(f"Name: {record["Name"]}")
             print(f"Roll no.: {record["Roll no"]}")
             print(f"Course: {record["Course"]}")
             print(f"Marks: {record["Marks"]}")
    else:
        print("No records found ")



def search():
    if records:
        y=input("Enter roll no. :")
        for index, student in enumerate(records):
            if y == student["Roll no"]:
    
              return index, student
    
        return None,None
    
    else :
        print("Invalid roll.no!!! unable to search")
        return None,None  
         
def update():
    index , student_found = search()
    if student_found is not None:
             print(f"Name: {student_found["Name"]}")
             print(f"Roll no.: {student_found["Roll no"]}")
             print(f"Course: {student_found["Course"]}")
             print(f"Marks: {student_found["Marks"]}")

             marks=input("Enter marks to update student marks :")

             records[index]["Marks"] = marks

             print("marks updated successfully")
    else:
        print("unable to search")

def delete():
        index , student_found = search()
        if index is not None:

            records.remove(student_found)
            print("Record deleted successfully")
        else:
            print("invalid roll no.!! unable to search")

def sort():
    if records:
        srt=input("Enter the choice of sorting record by name or marks :")
        if srt == "name":
            records.sort(key=lambda x:x["Name"] )
            print('records sorted successfully')
        
        elif srt == "marks":
            records.sort(key=lambda x: int(x["Marks"]), reverse =True)
            print('records sorted successfully')

        else:
            print('invalid')
while True :
    print("=================")
    print("1.Add Student")
    print("2.Display Student")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Sort Student")
    print("7.Exit")
    print("=================")

    ip=input("Enter your choice :")


    








    if ip == "1" :
# Add student
        add()

    elif ip == "2":
    # Display student
        dis()

    elif ip == "3":
    # Search student
        index, student = search()

        if student is not None:
            print(f"Name: {student["Name"]}")
            print(f"Roll no.: {student["Roll no"]}")
            print(f"Course: {student["Course"]}")
            print(f"Marks: {student["Marks"]}")
        else:
            print("Invalid roll.no!!! unable to search")
         
           
        
    elif ip == "4":
    # Update student
        update()

    elif ip == "5":
    # Delete student
        delete()

    elif ip == "6":
    # Sort student
        sort()

    elif ip == "7":
        print("Exitting program")
        break

    else :
        print("Invalid choice!!")
