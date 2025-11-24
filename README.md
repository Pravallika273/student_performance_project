# 🎓 **Student Performance Insights Dashboard**

# **A full-stack data analytics project aimed at predicting student academic success and reducing failure rates through actionable, visualized insights.**

# **Project Overview**

This project analyzes a **Student Performance Dataset (500 students, 12 features)** and builds a complete **end-to-end data analytics workflow** using Python, Scikit-Learn, and leading BI tools.

**Key Deliverables:**

  * **Exploratory Data Analysis (EDA)** and Feature Engineering
  * **Machine Learning Model** (Logistic Regression for Pass/Fail Prediction)
  * Interactive **Streamlit Dashboard** for live data exploration
  * Professional **Power BI Dashboard** for summary reporting
  * Complete Documentation & GitHub Deployment

-----

# **Dataset Summary**

| Column | Description | Data Range/Type |
| Student_ID | Unique student identifier | Identifier |
| Gender | Male/Female | Categorical |
| Age | Student age | 18–24 |
| Stream | Mech, ECE, EEE, CSE, Civil | Categorical |
| Attendance | Percentage attendance | 50–100% |
| Study_Hours | Daily study hours | Numerical |
| Internal_Marks | Marks from internal assessments | 0–30 |
| Final_Marks | Primary performance metric | 0–100 |
| Assignments_Submitted | Number of assignments submitted | 0–10 |
| Parental_Education | Low / Medium / High | Categorical |
| Internet_Access | Yes / No | Categorical |
| CGPA | Cumulative Grade Point Average | 0–10 |
| Pass | Derived column (1 if Final_Marks ≥ 40) | Binary (Target) |

-----

# **1️⃣ Exploratory Data Analysis (EDA)**

📁 Notebook: `EDA_student_performance.ipynb`

# **Key Insights**

1.  **Overall Pass Rate:** 59.6% of students passed.
2.  **Attendance vs Final Marks:** Low attendance clusters show poor marks, though the overall linear correlation is weak (r=0.09).
3.  **Stream-wise Performance:** Highest median performance in **ECE & Mech** streams; **Civil** shows the lowest median performance.
4.  **Internal Marks** (r=0.08) and **Study Hours** (r=0.15) show mild positive correlations with final performance.

-----

# **2️⃣ Feature Engineering & Model**

📁 Notebook: `model_student_performance.ipynb`

# **Feature Engineering**

  * Created the binary target variable `Pass`.
  * Categorized continuous features (e.g., created Attendance and Study Hour bands).
  * Standardized continuous features using `StandardScaler`.
  * **Exported cleaned dataset:** `student_performance_features.csv`

-----

# **Logistic Regression Model Results**

The model was trained to predict the `Pass` status.

Metric  | Value
Accuracy| 0.57
ROC AUC | 0.538

# **Model Interpretation**

  * The model achieves high **Recall (0.95)** for the 'Pass' class, indicating it is strong at identifying students who **will pass**.
  * The low overall accuracy and AUC suggest the model is weak at predicting **failures** (the At-Risk group). This indicates a need for more advanced features or different algorithms to improve sensitivity for low-performing students.

# **Top Predictors**

  * Attendance
  * Internal Marks
  * Study Hours

-----

# **3️⃣ Streamlit Dashboard**

📁 File: `app_streamlit.py`

# **Dashboard Features**

  * KPI Cards (Total Students, Pass Rate)
  * Final Marks Distribution
  * Stream-based filtering (Slicer)
  * **At-Risk Students Table** (Identifies low-scoring individuals)
  * Fully dynamic and interactive UI.

# **Run the App Locally**

```bash
streamlit run app_streamlit.py
```

-----

# **4️⃣ Power BI Dashboard**

**Visuals Included:**

  * KPI Cards (Student Count, Pass Rate)
  * **Average Final Marks by Stream** (Bar Chart)
  * **Final Marks by Attendance** (Line Chart)
  * **At-Risk Students Table** (Dynamic **Bottom 20** students ranked by Average Final Marks)
  * Slicers for Gender, Stream, and Parental Education.

-----

# **5️⃣ How to Run This Project Locally**

# **1. Clone the repository**

```bash
git clone https://github.com/pravallika273/student_performance_project.git
cd student_performance_project
```

# **2. Install dependencies**

```bash
pip install -r requirements.txt
```

# **3. Run JupyterLab**

```bash
jupyter lab
```

# **4. Launch the Streamlit Dashboard**

```bash
streamlit run app_streamlit.py
```

# **5. Open Power BI File**

Open `visuals.pbix` using Power BI Desktop.

-----

# **Project Images**

![Histogram](images\histogam.png) 
![Scatter Plot](images/scatter.png) 
![Boxplot](images/boxplot.png) 
![Streamlit Dashboard](http://192.168.0.106:8501) 
![Power BI Dashboard](images/visuals.png)

-----

# **Tech Stack**

  * Python (Pandas, NumPy, Matplotlib, Scikit-Learn)
  * Jupyter Notebook
  * Streamlit
  * Power BI
  * Git & GitHub

-----

# **Conclusion**

This project successfully demonstrates a full data analytics workflow—from **Data Cleaning** and **EDA** to **Machine Learning** and **Interactive Dashboards**. The result is a robust system that provides critical insights into student performance and facilitates data-driven decisions for academic intervention.

-----

# Author

**Pravallika**
MSc Data Science
