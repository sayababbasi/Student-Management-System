import pandas as pd

class ResultOfStudent():
    @classmethod
    def result(cls):
        df = pd.read_csv("gradesData.csv")
        print("Welcome to Results Section")
        key_id = input("For Checking Result, Enter Student ID: ").strip()

        # Convert "Student ID" column to string and check for existence
        if key_id not in df["Student ID"].astype(str).values:
            print("Student ID not found, Please Enter Correct ID")
            return  # Exit function if ID is not found

        # Filter dataframe based on Student ID
        df_filtered = df[df["Student ID"].astype(str) == key_id]
        print(df_filtered)

