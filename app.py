from collections import Counter
import re

st.subheader("Top Trending Words")

text_data = df['clean_text'].dropna().astype(str)

all_words = ' '.join(text_data)

words = re.findall(r'\w+', all_words.lower())

common_words = Counter(words).most_common(10)

for word, count in common_words:
    st.write(f"{word} : {count}")