import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

st.title("🧠 Simple Text Sentiment Analyzer")
st.write("Type any sentence and see the sentiment (Positive, Negative, or Neutral).")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0:
            sentiment = "😊 Positive"
        elif sentiment_score < 0:
            sentiment = "😞 Negative"
        else:
            sentiment = "😐 Neutral"

        st.success(f"Sentiment: **{sentiment}**")
        st.info(f"Sentiment Score: {sentiment_score:.2f}")
