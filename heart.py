import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.title('This is my project which was assigned by Eng: Abdel Rahman')
st.header("""The dataset contains the following columns:


1. age: The person's age in years
2. Sex: The person
3. chest_pain_type: The chest pain experienced by the person
4. resting_blood_pressure: The person's resting blood pressure (mm Hg on admission to the hospital)
5. cholestoral: The person's cholesterol measurement in mg/dl
6. fasting_blood_sugar: The person's fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
7. resting_elec_cardio_graphic: resting electrocardiographic results
8. max_heart_rate: The person's maximum heart rate achieved
9. exercise_induced_angina: Exercise induced angina (1 = yes; 0 = no)
10. st_depression: ST depression induced by exercise relative to rest
11. major_vessels: The number of major vessels (0-3) colored by fluoroscopy
12. thalassemia: A blood disorder called thalassemia
13. heart_disease: The person's heart disease (1 = no, 0 = yes )""")

st.code('This is a code section')
st.image(r"D:\Data since\Epsilon AI\DSP\Streamlit and dashboard\what-is-data-analysis.jpg")
df = pd.read_csv(r"D:\Data since\Epsilon AI\DSP\Streamlit and dashboard\cleaned_heart_dataset.csv")
st.dataframe(df)
if st.checkbox('Show the first 5 rows'):
    st.write(df.head())
if st.checkbox('Show the last 5 rows'):
    st.write(df.tail())
if st.button('Show top 5 Max Heart Rate'):
    st.write(df['max_heart_rate'].head(5).sort_values(ascending=False).reset_index(drop=True))
chest_pain = st.selectbox('chest pain type', [0, 1, 2, 3])
if chest_pain == 0:
    st.write(df[df['chest_pain_type'] == 0])
if chest_pain == 1:
    st.write(df[df['chest_pain_type'] == 1])
if chest_pain == 2:
    st.write(df[df['chest_pain_type'] == 2])
if chest_pain == 3:
    st.write(df[df['chest_pain_type'] == 3])
st.write(df['chest_pain_type'].value_counts(0))
filter_columns = st.multiselect('Select the columns to filter', df.columns)
if filter_columns:
    st.write(df[filter_columns])

st.sidebar.title('Data Visualization')
selected_column = st.sidebar.radio('Select the columns', ['sex', 'chest_pain_type', 'resting_blood_pressure', 'cholestoral', 'fasting_blood_sugar', 'resting_elec_cardio_graphic', 'max_heart_rate', 'exercise_induced_angina', 'st_depression', 'major_vessels', 'thalassemia', 'heart_disease'])

random = np.random.randn(1000, 2)
fig = px.histogram(random, x=random[:, 0], y=random[:, 1])
st.write('Histogram')
st.plotly_chart(fig)

df_tips = px.data.tips()
st.write('Bar Chart')
st.plotly_chart(px.bar(df_tips, x='day', y='total_bill', color='sex', barmode='group'))

st.write('Scatter Plot')
st.plotly_chart(px.scatter(df_tips, x='total_bill', y='tip', size='size', color='sex'))

st.write('bars Chart')
st.plotly_chart(px.bar(df_tips, x='total_bill', y='tip', color='sex'))
