import pandas as pd
import functions as fn


def print_heading(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    pd.set_option("display.width", 200)
    pd.set_option("display.max_columns", None)

    # ---- Step 1 & 2: Load and inspect the data ----
    df = fn.load_data("students.csv")

    print_heading("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print(f"Records loaded : {df.shape[0]}")
    print(f"Columns        : {', '.join(df.columns)}")

    print_heading("1. DATASET PREVIEW (first 5 records)")
    print(df.head().to_string(index=False))

    print_heading("2. DATASET INFO")
    df.info()

    # ---- Step 3: Process the data ----
    df = fn.calculate_total_and_average(df)
    df = fn.assign_grades(df)
    df = fn.check_pass_fail(df)
    df = fn.check_attendance(df)

    print_heading("3. FULL RESULT SHEET")
    print(df[["Student_ID", "Name", "Department", "Total", "Average",
              "Grade", "Result", "Attendance", "Attendance_Status"]].to_string(index=False))

    # ---- Step 4: Analysis ----
    stats = fn.class_statistics(df)
    print_heading("4. CLASS PERFORMANCE")
    print(f"Highest average : {stats['highest_name']} ({stats['highest_avg']})")
    print(f"Lowest average  : {stats['lowest_name']} ({stats['lowest_avg']})")
    print(f"Class average   : {stats['class_avg']}")
    print(f"Class median    : {stats['class_median']}")
    print(f"Std deviation   : {stats['std_dev']}")

    pf = fn.pass_fail_statistics(df)
    print_heading("5. PASS / FAIL STATISTICS")
    print(f"Total students  : {pf['total']}")
    print(f"Passed          : {pf['passed']}")
    print(f"Failed          : {pf['failed']}")
    print(f"Pass percentage : {pf['pass_percentage']}%")
    print("\nFailed students:")
    print(df[df["Result"] == "Fail"][["Student_ID", "Name", "Average"]].to_string(index=False))

    print_heading("6. GRADE DISTRIBUTION")
    for grade, count in fn.grade_distribution(df).items():
        print(f"Grade {grade:<3}: {'#' * count} ({count})")

    subj = fn.subject_analysis(df)
    print_heading("7. SUBJECT-WISE ANALYSIS")
    print(subj.to_string(index=False))
    best = subj.loc[subj["Average"].idxmax()]
    weak = subj.loc[subj["Average"].idxmin()]
    print(f"\nBest subject  : {best['Subject']} (avg {best['Average']})")
    print(f"Weakest subject: {weak['Subject']} (avg {weak['Average']})")

    print_heading("8. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df).to_string())

    print_heading("9. TOP 5 PERFORMING STUDENTS")
    print(fn.top_performers(df, 5).to_string(index=False))

    low_att = df[df["Attendance_Status"] == "Low"]
    print_heading("10. LOW ATTENDANCE STUDENTS (below 75%)")
    print(low_att[["Student_ID", "Name", "Attendance"]].to_string(index=False))

    # Save the processed results
    df.to_csv("results.csv", index=False)
    print("\nProcessed results saved to results.csv")


if __name__ == "__main__":
    main()
