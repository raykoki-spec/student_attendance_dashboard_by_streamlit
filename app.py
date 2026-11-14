"""Streamlit app that loads CSV file of a realistic
 sample data of class attendance in high school bsed in Nakuru.

Usage:
    streamlit run app.py

Output: dashboard that displays overall attendance,
 best attendance class, worst attendance class and
 line chart for attendance trend over the last 30 days.
"""
import streamlit as st
import pandas as pd

st.title("StateHouse Girls High School Nakuru")
st.write("Welcome to SGHS-NAKURU Attendance Dashboard")

attendance = pd.read_csv("attendance.csv")

attendance["attendance_rate"] = (
    attendance["students_present"] / attendance["students_total"] * 100
).round(1)

st.subheader("Daily Class Attendance")
st.dataframe(attendance)

overall_attendance = (
    attendance["students_present"].sum() / attendance["students_total"].sum() * 100
)

attendance_per_class = attendance.groupby("class_name")[["students_present", "students_total"]].sum()

class_rates = attendance_per_class["students_present"] / attendance_per_class["students_total"] * 100

best_attending_class = class_rates.idxmax()

worst_attending_class = class_rates.idxmin()

st.subheader("Class Attendance")

col1, col2, col3 = st.columns(3)

col1.metric("Overall Attendance", f"{overall_attendance:.1f}%")

col2.metric("Best Class", best_attending_class, f"{class_rates.max():.1f}%", delta_color="off")

col3.metric("Worst Class", worst_attending_class, f"{class_rates.min():.1f}%", delta_color="off")

attendance["date"] = pd.to_datetime(attendance["date"])

min_date = attendance["date"].min().date()

max_date = attendance["date"].max().date()

default_start = max(min_date, (attendance["date"].max() - pd.Timedelta(days=30)).date())

st.subheader("Filter")

date_range = st.slider(
    "Select date range",
    min_value=min_date,
    max_value=max_date,
    value=(default_start, max_date)

)

filtered = attendance[
    (attendance["date"] >= pd.to_datetime(date_range[0])) &
    (attendance["date"] <= pd.to_datetime(date_range)[1])
]

st.subheader("Showing Attendance Trend By Class")

chart_date = filtered.copy()

chart_date = chart_date.sort_values("date")

chart_data = chart_date.pivot(
    index="date",
    columns="class_name",
    values="attendance_rate",
).sort_index()

st.line_chart(chart_data)


uploaded = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.success(f"Loaded {len(df)} rows")
    st.dataframe(df.head(10))
else:
    st.info("Upload attendance CSV to get started. Or use the sample data below.")