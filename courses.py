import csv

import pandas as pd

class COURSES:

    COURSES_CSV = "coursesData.csv"
    COURSES_COLUMNS = ["Course Code", "Course Name", "Credit Hr", "Course Instructor", "Course Description"]

    @classmethod
    def load_course_csv(cls):
        try:
            df = pd.read_csv(cls.COURSES_CSV)
            if df.empty:
                df.to_csv(cls.COURSES_CSV, index=False)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COURSES_COLUMNS)
            df.to_csv(cls.COURSES_CSV, index=False)

    @classmethod
    def course_registration(cls, cid, cname, cr_hr, cinstructor, cdescription):
        new_registration = {
            "Course Code": cid,
            "Course Name": cname,
            "Credit Hr": cr_hr,
            "Course Instructor": cinstructor,
            "Course Description": cdescription
        }

        with open(cls.COURSES_CSV, "a", newline='') as cfile:
            writer = csv.DictWriter(cfile, fieldnames=cls.COURSES_COLUMNS)
            if cfile.tell() == 0:
                writer.writeheader()
            writer.writerow(new_registration)
        print(f"Course Name '{cname}' Successfully  Registered")


def enroll_courses():

    number_of_courses = int(input("How many courses you want to register: "))
    for i in range(number_of_courses):
        print("\n\t\tEnter Registration Details for Course " + str(i + 1) + ": \n")
        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")
        credit_hr = input("Enter credit hr: ")
        course_instructor = input("Enter course instructor: ")
        cdescription = input("Enter course description: ")

        print(f"RUN time {i+ 1}")
        COURSES.course_registration(course_code, course_name, credit_hr, course_instructor, cdescription)


