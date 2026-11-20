from pathlib import Path
import json

file = ("visitor.json")

def brouchure():
    print("------------------------------------------------------------/n")
    print("""Welcome to Cloud University!
Here you can learn about our courses, campus, and student community.
We hope you find the information you need.""")
    enrollment=["y","n"]
    enroll = input("would you like to enrol,Say y/n")
    if enroll == "n":
        print("------------------------------------------------------------/n")
        print("see you again, Thanks")
    else:
        visitor_entry()

def visitor_entry():
    
    visitor = {
                "name":input("please provide cadidate name as per government issued ID"),
                "qualification":input("please provide cadidate highest qualification"),
                }
  
    with open("visitor.json","a", encoding="UTF-8") as src:
        texts = json.load(src)
        


    with open("visitor.json",encoding="UTF-8") as dest:
        json.dump(visitor,dest,indent=2)
    