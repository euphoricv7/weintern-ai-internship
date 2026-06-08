# WeIntern AIML Internship — Week 1 Assignment
**Organization:** WeIntern Pvt Ltd


**Intern:** Vratika Kumawat

---

## Task Summary
| Task | Description | Status |
|------|-------------|--------|
| Task 1 | Data Cleaning & Analysis | ✅ Complete |
| Task 2 | Data Visualization Project | ✅ Complete |
| Task 3 | Business Insight Report | ✅ Complete |



## Task Summary

### Task 1: Student Performance Dataset Analysis
Performed data cleaning and preprocessing on a student performance dataset by handling missing values, removing duplicate records, standardizing categorical labels, and generating descriptive statistics. A cleaned dataset was prepared for further analysis.

### Task 2: Data Visualization and Analysis
Created multiple visualizations, including histograms, count plots, box plots, scatter plots, and a correlation heatmap, to explore score distributions, identify trends, and understand relationships between academic and behavioral factors.

### Task 3: Business Insight Report
Converted analytical findings into actionable business insights by identifying key performance drivers, providing recommendations for educators, discussing limitations, and highlighting the impact of data-driven decision-making in education.

---

## Dataset
- **Name:** Student Performance Dataset
- **Source:** Synthetically generated dataset for internship practice
- **Rows:** 200 (after cleaning) | **Columns:** 12
- **Target Variable:** FinalScore

---

## Libraries Used
- NumPy — numerical operations and array computations
- Pandas — data loading, cleaning, and analysis
- Matplotlib — chart creation and customization
- Seaborn — statistical visualizations

---

## Steps Performed
1. Loaded and inspected raw dataset
2. Created feature understanding table
3. Checked and reported missing values
4. Removed duplicate rows
5. Standardized inconsistent categorical labels
6. Filled missing values with median/Unknown
7. Checked and confirmed correct data types
8. Saved cleaned dataset separately
9. Computed descriptive statistics using NumPy and Pandas
10. Performed group comparisons by Gender, InternetAccess, ExtraActivities
11. Created 8 visualizations
12. Generated business insight report

---

## Key Findings
- Assignment scores show the strongest correlation with final scores (r = 0.90)
- Higher attendance is consistently linked with better academic performance
- Study hours show a moderate positive relationship with final scores (r = 0.74)
- Gender shows minimal impact on performance (Female: 36.25 vs Male: 37.24)
- Extra activities show negligible impact on final scores

---

## Visualizations
| Chart | Type | File |
|-------|------|------|
| Distribution of Final Scores | Histogram | outputs/charts/score_distribution.png |
| Students by Gender | Count Plot | outputs/charts/gender_distribution.png |
| Internet Access Distribution | Count Plot | outputs/charts/internet_distribution.png |
| Final Score by Extra Activities | Box Plot | outputs/charts/score_by_activities.png |
| Final Score by Gender | Box Plot | outputs/charts/score_by_gender.png |
| Study Hours vs Final Score | Scatter Plot | outputs/charts/study_vs_score.png |
| Attendance vs Final Score | Scatter Plot | outputs/charts/attendance_vs_score.png |
| Correlation Heatmap | Heatmap | outputs/charts/correlation_heatmap.png |

---

## Folder Structure
```
aiml-week1-assignment/
├── data/
│   ├── raw/                          
│   └── cleaned/                      
├── notebooks/
│   ├── Task1_Student_Performance_Analysis.ipynb
│   ├── Task2_Data_Visualization.ipynb
│   └── Task3_Business_Insight_Report.ipynb
├── outputs/
│   └── charts/                       
├── screenshots/
├── README.md
└── requirements.txt
```

---

## How to Run
### Task 1 — Data Cleaning & Analysis
1. Open Google Colab — [colab.research.google.com](https://colab.research.google.com)
2. Upload `notebooks/Task1_Student_Performance_Analysis.ipynb`
3. Upload `data/raw/student_performance.csv`
4. Click **Runtime → Run All**

### Task 2 — Data Visualization
1. Open Google Colab — [colab.research.google.com](https://colab.research.google.com)
2. Upload `notebooks/Task2_Data_Visualization.ipynb`
3. Upload `data/cleaned/student_performance_cleaned.csv`
4. Click **Runtime → Run All**

### Task 3 — Business Insight Report
1. Open Google Colab — [colab.research.google.com](https://colab.research.google.com)
2. Upload `notebooks/Task3_Business_Insight_Report.ipynb`
3. No dataset needed — report is text only
4. Click **Runtime → Run All**

### **Tip:** To open directly in Colab, replace 
`github.com` with `githubtocolab.com` in the file URL 
---

## Author
**Vratika Kumawat** | WeIntern AIML Internship 2025
