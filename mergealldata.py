# import pandas as pd
#
# # Load the CSV files into pandas DataFrames
# student_data = pd.read_csv("studentsData.csv")
# course_data = pd.read_csv("coursesData.csv")
# grade_data = pd.read_csv("gradesData.csv")
#
# # Merge the student data with grade data on 'Student ID'
# merged_data = pd.merge(grade_data, student_data, on='Student ID', how='left')
#
# # Merge the result with course data on 'Course' (assuming 'Course' in grade_data maps to 'Course Name' in course_data)
# final_data = pd.merge(merged_data, course_data, left_on='Course', right_on='Course Name', how='left')
#
# # Save the final merged data into a new CSV file
# final_data.to_csv("merged_student_course_grade_data.csv", index=False)
#
# print("Data merged successfully and saved to 'merged_student_course_grade_data.csv'.")

import pandas as pd

# Load the CSV files into pandas DataFrames
student_data = pd.read_csv("studentsData.csv")
course_data = pd.read_csv("coursesData.csv")
grade_data = pd.read_csv("gradesData.csv")

# Clean up column names (strip spaces or remove any extra characters if necessary)
student_data.columns = student_data.columns.str.strip()
course_data.columns = course_data.columns.str.strip()
grade_data.columns = grade_data.columns.str.strip()

# Make sure Student ID is treated as a string to avoid any potential type mismatches
student_data['Student ID'] = student_data['Student ID'].astype(str)
grade_data['Student ID'] = grade_data['Student ID'].astype(str)

# Merge the student data with grade data on 'Student ID'
merged_data = pd.merge(grade_data, student_data, on='Student ID', how='left')

# Merge the result with course data on 'Course' (assuming 'Course' in grade_data maps to 'Course Name' in course_data)
final_data = pd.merge(merged_data, course_data, left_on='Course', right_on='Course Name', how='left')

# Select only the necessary columns
final_data = final_data[['Student ID', 'Student Name', 'Student Department', 'Course', 'Grade', 'Course Code', 'Credit Hr', 'Course Instructor']]

# Save the final merged data into a new CSV file
final_data.to_csv("Students_Complete_DATABASE.csv", index=False)

print(f"Data merged successfully and saved to 'Students_Complete_DATABASE.csv'.")
