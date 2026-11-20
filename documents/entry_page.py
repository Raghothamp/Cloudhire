from pathlib import Path
#from documents import explore
from explore import brouchure
from student import student_details
import csv,json

print("Welcome to Cloud university!!!")
choice1 = ["explore","student"]

choice =input("Exploring cloud university ? or already in Aluminy ?,type Explore or Student ")
if choice.lower() == "explore":
    print("------------------------------------------------------------/n")
    print("/n Thank you lets explore more. /n")
    brouchure()

elif choice.lower() == "student":
    print("------------------------------------------------------------/n")
    print("please provide student ID")
    student_details()
else:
    print("Thank you ! visit again")