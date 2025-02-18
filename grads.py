import csv

import pandas as pd
from win32trace import write


class GRADE:

    GRADE_CSV = "gradesData.csv"
    GRADES_COLUMS = ["Student ID", "Student Name", "Student Department", "Course", "Grade"]
    @classmethod
    def load_grade_csv(cls):
        try:
            df = pd.read_csv(cls.GRADE_CSV)
            if df.empty:
                df.to_csv(cls.GRADE_CSV, index=False)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.GRADES_COLUMS)
            df.to_csv(cls.GRADE_CSV, index=False)

    @classmethod
    def add_grades(cls, sid, sname, sdept, course, grade):
        new_grades_entry = {
            "Student ID": sid,
            "Student Name": sname,
            "Student Department": sdept,
            "Course": course,
            "Grade": grade
        }

        with open(cls.GRADE_CSV, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=cls.GRADES_COLUMS)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(new_grades_entry)
        print(f"Student {sname} Grade Added Successfully!")

# GRADE.add_grades(12345,"SAYAB","BS AI","WL","C+")