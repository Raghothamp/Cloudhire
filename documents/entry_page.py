from pathlib import Path
#from documents import explore
from explore import brouchure
from student import student_details
import csv,json

print("Welcome to Cloud university!!!")
choice1 = ["explore","student"]

choice =input("Tell us more !!Are you visiting cloud university for first time? or are u a part of it ?Please type 1.'Explore' or 2.'Student' to proceed : ")
if choice.lower() == "explore":
    print("------------------------------------------------------------")
    print(" Thank you lets explore more. ")
    brouchure()

elif choice.lower() == "student":
    print("------------------------------------------------------------")
    print("please provide student ID : ")
    student_details()
else:
    print("Thank you ! visit again")