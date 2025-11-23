import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_features.csv")
st.title("Student Performance Dashboard")
st.metric("Students", len(df))
st.metric("Pass rate", f"{df['Pass'].mean():.2%}")

stream = st.sidebar.multiselect("Stream", df['Stream'].unique(), default=list(df['Stream'].unique()))
df_f = df[df['Stream'].isin(stream)]

st.subheader("Final Marks Distribution")
fig, ax = plt.subplots()
ax.hist(df_f['Final_Marks'], bins=20)
st.pyplot(fig)

st.subheader("At-Risk Students (lowest final marks)")
st.table(df_f.sort_values('Final_Marks').head(10)[['Student_ID','Final_Marks','Attendance','Study_Hours','CGPA']])
