# student-performance-analytics
# 1. Project Title
**Student Performance Analytics System**

- Student Name: _<ved prakash kumawat>_
- Course: Python with AI – EWB Courses

# 2. Objective
Teachers often have raw marks in a spreadsheet but no quick way to see how the class is doing.
This project reads student data and automatically calculates totals, averages, grades,
pass/fail status, subject-wise and department-wise performance, and identifies the top performers.

# 3. Technologies Used
- Python 3
- NumPy – numerical calculations (sum, mean, median, std, max/min, conditions)
- Pandas – loading the CSV, DataFrame operations, grouping and sorting

# 4. Dataset Description
`students.csv` contains **20 student records** with these columns:

| Column | Description |
|---|---|
| Student_ID | Unique ID (S001–S020) |
| Name | Student name |
| Department | Computer Science, Electronics, Mechanical, Civil |
| Maths, Physics, Chemistry, English, Computer_Science | Marks out of 100 |
| Attendance | Attendance percentage |

# 5. Implementation
1. **Load data** – `load_data()` reads the CSV into a Pandas DataFrame; shape, columns and `info()` are displayed.
2. **Totals & averages** – `calculate_total_and_average()` converts the marks to a NumPy array and uses `np.sum` / `np.mean` with `axis=1`.
3. **Grades** – `assign_grades()` loops over each average and calls `get_grade()`.

   | Average | Grade |
   |---|---|
   | 90+ | A+ |
   | 80–89 | A |
   | 70–79 | B |
   | 60–69 | C |
   | 50–59 | D |
   | 40–49 | E |
   | below 40 | F |
4. **Pass/Fail rule** – a student passes only if they score **at least 40 in every subject** (`check_pass_fail()` uses NumPy `np.where`).
5. **Attendance** – attendance below 75% is flagged as "Low".
6. **Analysis** – class statistics, pass percentage, grade distribution, subject-wise analysis, department-wise analysis and top 5 students.
7. **Output** – results are printed in readable sections and saved to `results.csv`.

# 6. Key Features
- `load_data()` – read CSV
- `calculate_total_and_average()` – totals/averages with NumPy
- `get_grade()` / `assign_grades()` – grading rule
- `check_pass_fail()` / `check_attendance()` – status checks
- `class_statistics()` – highest, lowest, average, median, std deviation
- `pass_fail_statistics()` – pass count and percentage
- `subject_analysis()` – per-subject average, highest, lowest, failures
- `department_analysis()` – grouped summary using Pandas `groupby`
- `top_performers()` – ranking of best students

# 7. How to Run
```bash
pip install numpy pandas
python main.py
```
A full sample of the output is in `sample_output.txt`. _(Add screenshots here.)_

# 8. Final Outcome
For the 20-student dataset the program found:
- Highest average: **Sneha Joshi (92.6)**; lowest: Harsh Pareek (39.0)
- Class average: **69.89**
- **17 passed, 3 failed** (85% pass rate)
- Best subject: **English (73.4)**; weakest: Physics (67.85)
- Best department: Computer Science (85.04 average)

The project successfully turns raw marks into clear, readable insights.

# 9. Challenges & Learning
_<Write this in your own words: problems you faced, how you solved them, what you learned.>_

# 10. GitHub Repository
_<(https://github.com/vedprakash3280/student-performance-analytics)>_
