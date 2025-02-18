from students_registration import StudentRegistration
from grads import GRADE
from result_of_student import ResultOfStudent
from courses import COURSES


def new_student_entry():
    """Registers a new student by taking input and passing it to the StudentRegistration class."""
    try:
        sid = input("Enter student ID: ").strip()
        first_name = input("Enter First Name: ").strip()
        last_name = input("Enter Last Name: ").strip()
        age = input("Enter Age: ").strip()
        contact_number = input("Enter Contact Number: ").strip()
        email_address = input("Enter Email Address: ").strip()
        address = input("Enter Address: ").strip()

        if not all([sid, first_name, last_name, age, contact_number, email_address, address]):
            print("All fields are required. Please try again.")
            return

        StudentRegistration().add_student(sid, first_name, last_name, age, contact_number, email_address, address)
        print("Student registered successfully!")
    except Exception as e:
        print(f"Error: {e}")


def m_add_grade():
    """Adds grades for a student."""
    try:
        sid = input("Enter student ID: ").strip()
        sname = input("Enter Student Name: ").strip()
        sdept = input("Enter Student Department: ").strip()
        course = input("Enter Courses: ").strip()
        grade = input("Enter Grade: ").strip()

        if not all([sid, sname, sdept, course, grade]):
            print("All fields are required. Please try again.")
            return

        GRADE().add_grades(sid, sname, sdept, course, grade)
    except Exception as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\n\t\tWelcome to SAYAB TECHNICAL UNIVERSITY")
        print("1. Student Registration")
        print("2. Course Registration")
        print("3. Enrollment")
        print("4. Grades")
        print("5. Result")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: ").strip())

            if choice == 1:
                new_student_entry()
            elif choice == 2:
                COURSES().course_registration()
            elif choice == 3:
                COURSES().enroll_courses()
            elif choice == 4:
                m_add_grade()
            elif choice == 5:
                ResultOfStudent().result()
            elif choice == 6:
                print("Thank you for using our ONLINE SYSTEM. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
