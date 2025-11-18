# 📌 AI Employee Sentiment Analysis Project
Final LLM Assessment — NLP + EDA + Regression Modeling

This project analyzes unlabeled employee messages and performs:

Sentiment labeling

Exploratory data analysis (EDA)

Monthly sentiment scoring

Employee ranking

Flight risk detection

Predictive modeling (Linear Regression)

## 📂 Project Structure
ai-project/
├─ data/
│  └─ test.csv
├─ notebooks/
│  └─ sentiment_analysis.ipynb
├─ src/
│  ├─ data_utils.py
│  ├─ sentiment_labeler.py
│  ├─ scoring.py
│  ├─ flightrisk.py
│  └─ modeling.py
├─ visualizations/
│  └─ (generated charts)
├─ requirements.txt
├─ README.md
├─ .env.example
└─ final_report.docx

## 🚀 How to Run This Project
1️⃣ Install all required libraries
pip install -r requirements.txt

2️⃣ Open the main notebook
notebooks/sentiment_analysis.ipynb

3️⃣ Run the notebook cells in sequence

This performs:

Loading the dataset

Sentiment analysis

EDA

Monthly scoring

Ranking employees

Flight risk detection

Linear regression modeling

## 🧠 Task Summary
### 1️⃣ Sentiment Labeling

Using TextBlob, each message is classified as:

Positive

Negative

Neutral

Sentiment is computed on:

Subject + body


Output column added:

sentiment

### 2️⃣ Exploratory Data Analysis (EDA)

Performed analysis includes:

Total number of messages

Missing values check

Message length distribution

Sentiment distribution

Top message senders

Time series trends

Heatmaps and bar charts

All visualizations are saved in:

visualizations/

### 3️⃣ Monthly Sentiment Score

Each message is assigned:

Sentiment	Score
Positive	+1
Neutral	0
Negative	–1

Then grouped by:

employee_id + month


Output columns:

employee_id | month | sentiment_score

### 4️⃣ Employee Ranking

For each month:

Top 3 positive employees

Top 3 negative employees

Ranking based on sentiment score, and ties resolved alphabetically.

### 5️⃣ Flight Risk Detection

Flight risk criteria:

Any employee who sends 4 or more negative messages in a rolling 30-day period.

Output:

flight_risk_list.csv

### 6️⃣ Predictive Modeling (Linear Regression)

Independent features used:

Message length

Word count

Monthly message frequency

Average message length

Model:

Linear Regression (sklearn)


Evaluated using:

R² Score

MAE

MSE

## 📊 Visualizations

All plots are exported automatically into:

visualizations/


Examples:

Sentiment distribution pie chart

Monthly sentiment trends

Employee ranking charts

Regression diagnostic plots

## 📝 Final Report

Located inside:

final_report.docx


Contains:

Methodology

Key findings

EDA insights

Ranking summary

Flight risk list

Model evaluation

Conclusion
