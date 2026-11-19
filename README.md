
# Student Attendance Dashboard: StateHouse Girls High School, Nakuru

A Streamlit web app that lets the school principal monitor student attendance of 5 classes from a phone or laptop, without opening Excel.

image.png

## What It Does

- Connects to the CSV file
- Applies logic to produce key metrics (overall attendance rate, best attending class, worst attending class) 
- Plots a line chart of attendance rate per class
- Filters the date with date_range slider
- The dashboard displays key metrics and line charts and also accepts other attendance CSV file upload to analyze


## Usage

Run the program from the project's folder where the attendance.csv file is saved. 
```
streamlit run app.py
```

## Setup

```bash
pip install -r requirements.txt
```

## How It Works

```python
attendance = pd.read_csv("attendance.csv") - Connects to the CSV file

col1, col2, col3 = st.columns(3) - Creates 3 columns that display key metrics

col1.metric("Overall Attendance", f"{overall_attendance:.1f}%")

col2.metric("Best Class", best_attending_class, f"{class_rates.max():.1f}%", delta_color="off")

col3.metric("Worst Class", worst_attending_class, f"{class_rates.min():.1f}%", delta_color="off")
```

## CSV Format

The CSV needs these four columns (header row required):

| Column | Description | Example |
|---|---|---|
| `date` | Day of the record, `YYYY-MM-DD` | `2026-03-02` |
| `class_name` | Class name | `Grade 9` |
| `students_present` | Students present that day | `36` |
| `students_total` | Students enrolled in the class | `40` |

One row per class per day.

## Stack

- **Python**: core language
- **Streamlit**: web interface (metrics, date slider, charts, runs in the browser on phone or laptop)
- **pandas**: loading the CSV and calculating attendance rates

