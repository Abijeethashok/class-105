import csv
import plotly.graph_objects as go
import pandas as pd

studentID = input("ENTER STUDENT ID")

df = pd.read_csv("student.csv")

studentds = df.loc[df['student_id']== studentID]

print(studentds.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(x = studentds.groupby("level")["attempt"].mean(), y = ['level 1','level 2','level 3','level 4'], orientation = 'h'))

fig.show()