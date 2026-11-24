from pathlib import Path
import json
from student import enrol_stud
file = Path(__file__).with_name("visitor.json")

def brouchure():
    print("------------------------------------------------------------")
    print("""Welcome to Cloud University!
Here you can learn about our courses, campus, and student community.
We hope you find the information you need.""")
    enrollment=["y","n"]
    enroll = input("would you like to enrol to cloudhire ,Please respond with y/n : ")
    if enroll == "n":
        print("------------------------------------------------------------")
        print("see you again, Thanks")
    else:
        visitor_entry()

def visitor_entry():
    
    visitor = { "name":input("please provide cadidate name as per government issued ID : "),
                "qualification":input("please provide cadidate highest qualification : "),}
    if file.exists() and file.stat().st_size > 0:
        with file.open("r", encoding="UTF-8") as src:
            visitors = json.load(src)
        # Convert a single visitor saved by the earlier version into a list.
        if isinstance(visitors, dict):
            visitors = [visitors]
    else:
        visitors = []
    visitors.append(visitor)

    with file.open("w",encoding="UTF-8") as dest:
            json.dump(visitors,dest,indent=2)

    student = enrol_stud(visitor)
    print(f"Your details are registered. Your StudentID is {student['StudentID']}.")
    
