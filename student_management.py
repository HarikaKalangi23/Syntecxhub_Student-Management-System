import json
import os


# Student class
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


# Student Manager class
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    # Load students from JSON file
    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    data = json.load(file)

                    self.students = [
                        Student(
                            item["id"],
                            item["name"],
                            item["grade"]
                        )
                        for item in data
                    ]

                except json.JSONDecodeError:
                    self.students = []

    # Save students to JSON file
    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(
                [student.to_dict() for student in self.students],
                file,
                indent=4
            )

    # Add a new student
    def add_student(self, student_id, name, grade):

        # Check for duplicate ID
        for student in self.students:
            if student.student_id == student_id:
                print("\nError: Student ID already exists!")
                return

        student = Student(student_id, name, grade)
        self.students.append(student)

        self.save_students()

        print("\nStudent added successfully!")

    # Display all students
    def list_students(self):

        if not self.students:
            print("\nNo student records found.")
            return

        print("\n" + "=" * 55)
        print("                 STUDENT RECORDS")
        print("=" * 55)

        print(f"{'ID':<12}{'NAME':<25}{'GRADE':<10}")
        print("-" * 55)

        for student in self.students:
            print(
                f"{student.student_id:<12}"
                f"{student.name:<25}"
                f"{student.grade:<10}"
            )

        print("=" * 55)

    # Update student details
    def update_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:

                print("\nStudent found!")

                new_name = input(
                    "Enter new name: "
                ).strip()

                new_grade = input(
                    "Enter new grade: "
                ).strip()

                if new_name:
                    student.name = new_name

                if new_grade:
                    student.grade = new_grade

                self.save_students()

                print("\nStudent updated successfully!")
                return

        print("\nStudent ID not found!")

    # Delete a student
    def delete_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:

                self.students.remove(student)

                self.save_students()

                print("\nStudent deleted successfully!")
                return

        print("\nStudent ID not found!")


# Main program
def main():

    manager = StudentManager()

    while True:

        print("\n")
        print("=" * 55)
        print("             STUDENT MANAGEMENT SYSTEM")
        print("=" * 55)

        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Student")
        print("5. Exit")

        print("=" * 55)

        choice = input("Enter your choice (1-5): ").strip()

        # Add Student
        if choice == "1":

            print("\n--- ADD STUDENT ---")

            student_id = input(
                "Enter Student ID: "
            ).strip()

            name = input(
                "Enter Student Name: "
            ).strip()

            grade = input(
                "Enter Student Grade: "
            ).strip()

            if not student_id or not name or not grade:
                print("\nError: All fields are required!")
            else:
                manager.add_student(
                    student_id,
                    name,
                    grade
                )

        # Update Student
        elif choice == "2":

            print("\n--- UPDATE STUDENT ---")

            student_id = input(
                "Enter Student ID to update: "
            ).strip()

            manager.update_student(student_id)

        # Delete Student
        elif choice == "3":

            print("\n--- DELETE STUDENT ---")

            student_id = input(
                "Enter Student ID to delete: "
            ).strip()

            manager.delete_student(student_id)

        # List Students
        elif choice == "4":

            manager.list_students()

        # Exit
        elif choice == "5":

            print("\nThank you for using")
            print("Student Management System!")

            break

        # Invalid choice
        else:

            print("\nInvalid choice!")
            print("Please enter a number between 1 and 5.")


# Start program
if __name__ == "__main__":
    main()