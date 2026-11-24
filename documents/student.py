import json
from pathlib import Path
from uuid import uuid4


DATA_FILE = Path(__file__).resolve().parent / "data" / "records.json"


def enrol_stud(visitor):
    """Create a student record from submitted visitor details and save it."""
    student = {
        "StudentID": f"STU-{uuid4().hex[:8].upper()}",
        "name": visitor["name"].strip(),
        "qualification": visitor["qualification"].strip(),
    }

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if DATA_FILE.exists() and DATA_FILE.stat().st_size > 0:
        with DATA_FILE.open("r", encoding="UTF-8") as src:
            records = json.load(src)
    else:
        records = {"students": []}

    # Recover gracefully if the file exists but is an empty list or has no students key.
    if isinstance(records, list):
        records = {"students": records}
    records.setdefault("students", []).append(student)

    with DATA_FILE.open("w", encoding="UTF-8") as dest:
        json.dump(records, dest, indent=2)

    return student


def student_details():
    print("Please provide student details")
    visitor = {
        "name": input("Name as per Government ID: "),
        "qualification": input("Highest degree achieved: "),
    }
    student = enrol_stud(visitor)
    print(f"Student registered. Your StudentID is {student['StudentID']}")
