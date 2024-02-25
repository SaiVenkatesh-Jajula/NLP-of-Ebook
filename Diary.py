import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px
import glob
from pathlib import Path
import re

analyzer = SentimentIntensityAnalyzer()
positivescore = []
negativescore = []
dates = []
filepaths = [Path(i) for i in glob.glob("Diary/*.txt")]

# Extract dates

for filepath in filepaths:
    pattern = re.compile("[0-9 -]")
    date = re.findall(pattern, str(filepath))
    date = "".join(date)
    dates.append(date)
    with open(filepath, 'r') as file:
        diarynotes = file.read()
    analysis = analyzer.polarity_scores(diarynotes)
    positivescore.append(analysis['pos'])
    negativescore.append(analysis['neg'])

st.title("Diary Tone")

st.subheader("Positivity")
figure1 = px.line(x=dates, y=positivescore, labels={'x': 'Dates', 'y': 'Positivity'})
st.plotly_chart(figure1)

st.subheader("negativity")
figure2 = px.line(x=dates, y=negativescore, labels={'x':'Dates', 'y':'Negativity'})
st.plotly_chart(figure2)