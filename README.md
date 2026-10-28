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
_<Using NumPy with a Pandas DataFrame.
At first I was unsure how to calculate totals and averages for each student. I learned to convert the subject columns into a NumPy array with to_numpy() and use np.sum() and np.mean() with axis=1 to calculate row-wise results.
Deciding the grading and pass/fail rules.
The project did not give a fixed rule, so I had to define one. I used average marks for grades (A+ for 90 and above, down to F below 40) and made a student pass only if they scored at least 40 in every subject. This made the results more meaningful than only using the total.
Organizing the code.
Keeping everything in one file made it confusing. I moved all the calculations into functions.py and kept main.py only for displaying results. This made the code cleaner and easier to reuse.
Creating a realistic dataset.
I had to make 20 records with realistic marks and attendance, including some students who fail and some with low attendance, so the analysis would show useful differences.
Using GitHub.
As a beginner, I had to learn how to create a repository, commit files and publish them using GitHub Desktop.

What I learned

How to load and explore data using Pandas DataFrames
How to use NumPy for fast numerical calculations
How to write reusable functions and use loops and conditions
How to analyze data with grouping, sorting and filtering
How to organize a project and document it properly
How to use Git and GitHub to submit a project.>_

# 10. GitHub Repository
_<(https://github.com/vedprakash3280/student-performance-analytics)>_
