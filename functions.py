import numpy as np
import pandas as pd

# ---------- Configuration (clearly defined rules) ----------
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer_Science"]
PASS_MARK = 40            # a student must score at least 40 in EVERY subject to pass
MIN_ATTENDANCE = 75       # attendance (%) below this is flagged as "Low"

# Grading rule based on average marks: (minimum average, grade)
GRADING_RULE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (40, "E"),
]


def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total_and_average(df):
    """Add Total and Average columns using NumPy on the subject marks."""
    marks = df[SUBJECTS].to_numpy()                    # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)                # row-wise total
    df["Average"] = np.round(np.mean(marks, axis=1), 2)  # row-wise average
    return df


def get_grade(average):
    """Return the grade for one student's average using GRADING_RULE."""
    for minimum, grade in GRADING_RULE:
        if average >= minimum:
            return grade
    return "F"


def assign_grades(df):
    """Assign a grade to every student (loop over the Average column)."""
    grades = []
    for avg in df["Average"]:
        grades.append(get_grade(avg))
    df["Grade"] = grades
    return df


def check_pass_fail(df):
    """Pass only if the student scored >= PASS_MARK in every subject."""
    all_subjects_passed = (df[SUBJECTS].to_numpy() >= PASS_MARK).all(axis=1)
    df["Result"] = np.where(all_subjects_passed, "Pass", "Fail")
    return df


def check_attendance(df):
    """Flag attendance as OK or Low based on MIN_ATTENDANCE."""
    df["Attendance_Status"] = np.where(df["Attendance"] >= MIN_ATTENDANCE, "OK", "Low")
    return df


def class_statistics(df):
    """Return highest, lowest and average performance of the class."""
    top = df.loc[df["Average"].idxmax()]
    bottom = df.loc[df["Average"].idxmin()]
    return {
        "highest_name": top["Name"],
        "highest_avg": top["Average"],
        "lowest_name": bottom["Name"],
        "lowest_avg": bottom["Average"],
        "class_avg": round(float(np.mean(df["Average"])), 2),
        "class_median": round(float(np.median(df["Average"])), 2),
        "std_dev": round(float(np.std(df["Average"])), 2),
    }


def pass_fail_statistics(df):
    """Return counts and percentage of pass/fail students."""
    total = len(df)
    passed = int((df["Result"] == "Pass").sum())
    failed = total - passed
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_percentage": round(passed / total * 100, 2),
    }


def subject_analysis(df):
    """Subject-wise average, highest, lowest and number of students failing."""
    rows = []
    for subject in SUBJECTS:
        column = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(column)), 2),
            "Highest": int(np.max(column)),
            "Lowest": int(np.min(column)),
            "Failed_Students": int(np.sum(column < PASS_MARK)),
        })
    return pd.DataFrame(rows)


def department_analysis(df):
    """Average marks, attendance and pass count for each department."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Avg_Attendance=("Attendance", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2)
    return summary.sort_values("Avg_Marks", ascending=False)


def top_performers(df, n=5):
    """Return the top n students ranked by average marks."""
    top = df.sort_values("Average", ascending=False).head(n)
    return top[["Student_ID", "Name", "Department", "Total", "Average", "Grade"]]


def grade_distribution(df):
    """Count of students in each grade."""
    return df["Grade"].value_counts().sort_index()
