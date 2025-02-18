import csv

import  pandas as pd



class StudentRegistration:

    STUDENT_CSV = "studentsData.csv"
    COLUMNS = ["Student ID", "First Name", "Last Name", "Age", "Contact Number", "Email Address", "Address"]

    @classmethod
    def load_student_csv(cls):
        # Store CSV FILE DATA INTO DATAFRAME DF
        try:
            df = pd.read_csv(cls.STUDENT_CSV)
            if df.empty:
               df.to_csv(cls.STUDENT_CSV, index=False)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.STUDENT_CSV, index=False)


    @classmethod
    def add_student(cls,student_id, first_name, last_name, age, contact, email, address):
        new_entry = {
            "Student ID": student_id,
            "First Name": first_name,
            "Last Name": last_name,
            "Age": age,
            "Contact Number": contact,
            "Email Address": email,
            "Address": address
        }

        with open(cls.STUDENT_CSV, "a", newline='') as style:
            writer = csv.DictWriter(style, fieldnames=cls.COLUMNS)
            if style.tell() == 0:
                writer.writeheader()
            writer.writerow(new_entry)
        print(f"{first_name} {last_name} Is Successfully Registered as a Student")

