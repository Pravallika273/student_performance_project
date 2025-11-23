# generate_dataset.py
import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

data = {
    "Student_ID": [f"S{1000+i}" for i in range(n)],
    "Gender": np.random.choice(["Male", "Female"], n),
    "Age": np.random.randint(18, 25, n),
    "Stream": np.random.choice(["CSE", "ECE", "EEE", "Civil", "Mech"], n),
    "Attendance": np.random.randint(50, 101, n),
    "Study_Hours": np.round(np.random.uniform(0, 6, n), 1),
    "Internal_Marks": np.random.randint(0, 31, n),
    "Final_Marks": np.random.randint(0, 101, n),
    "Assignments_Submitted": np.random.randint(0, 11, n),
    "Parental_Education": np.random.choice(["Low", "Medium", "High"], n),
    "Internet_Access": np.random.choice(["Yes", "No"], n),
    "CGPA": np.round(np.random.uniform(0, 10, n), 2)
}

df = pd.DataFrame(data)
df.to_csv("student_performance.csv", index=False)
print("student_performance.csv created with", len(df), "rows")
