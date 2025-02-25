# s student_management.py

def student_names():
    """Stores and displays a list of student names."""
    students = ["John", "Emma", "Sophia", "Michael", "Daniel"]
    students.append("Olivia")  # Adding a new student
    return students

def student_courses():
    """Stores student course enrollments using a dictionary."""
    courses = {
        "John": ("Math", "Physics"),
        "Emma": ("Biology", "Chemistry"),
        "Sophia": ("History", "English"),
        "Michael": ("Math", "Computer Science"),
        "Daniel": ("Physics", "Chemistry")
    }
    courses["Olivia"] = ("Biology", "History")  # Adding a new student course
    return courses

def unique_subjects():
    """Stores and displays unique subjects from all students using a set."""
    all_subjects = {"Math", "Physics", "Biology", "Chemistry", "English", "History", "Computer Science", "Math"}
    all_subjects.add("Economics")  # Adding a new subject
    return all_subjects

# Call functions and print their output
print("Student Names:", student_names())
print("Student Courses:", student_courses())
print("Unique Subjects:", unique_subjects())
