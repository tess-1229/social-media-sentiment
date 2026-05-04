import streamlit as st
import pandas as pd
from collections import Counter
import re

st.title("📊 Social Media Analytics System")

# Load dataset
df = pd.read_csv("social_media.csv")

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Sentiment distribution
st.subheader("Sentiment Distribution")
sentiment_count = df['AI_Sentiment'].value_counts()
st.bar_chart(sentiment_count)

# Trending words
st.subheader("Top Trending Words")
text_data = df['clean_text'].astype(str)
all_words = ' '.join(text_data)
words = re.findall(r'\w+', all_words.lower())

common_words = Counter(words).most_common(10)

for word, count in common_words:
    st.write(f"{word} : {count}")