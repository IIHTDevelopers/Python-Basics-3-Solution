# student_marks_analysis.py

import numpy as np

def analyze_marks(marks):
    """Computes basic statistics for student marks."""
    avg_marks = np.mean(marks)
    max_marks = np.max(marks)
    min_marks = np.min(marks)
    return avg_marks, max_marks, min_marks

def classify_grades(marks):
    """Classifies students based on their marks."""
    grades = []
    for mark in marks:
        if mark >= 90:
            grades.append("A")
        elif mark >= 80:
            grades.append("B")
        elif mark >= 70:
            grades.append("C")
        else:
            grades.append("D")
    return grades

# Preset student marks for 5 students
student_marks = np.array([78, 85, 92, 88, 76])

# Analyze student marks
avg_marks, max_marks, min_marks = analyze_marks(student_marks)
grades = classify_grades(student_marks)

# Display results
print("Student Marks Analysis")
print(f"Marks: {student_marks}")
print(f"Average Marks: {avg_marks:.2f}")
print(f"Highest Marks: {max_marks}")
print(f"Lowest Marks: {min_marks}")
print(f"Student Grades: {grades}")
