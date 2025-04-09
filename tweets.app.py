import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the data
tweets = pd.read_csv('https://raw.githubusercontent.com/Md-Arshad-Khan/MdArshadKhan-tweets/main/Tweets.csv')

# Streamlit app
st.title("Airline Tweets Analysis")

# Sentiment Distribution Pie Chart
st.subheader("Sentiment Distribution")
sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['airline_sentiment', 'count']
fig_pie = px.pie(sentiment_counts, values='count', names='airline_sentiment', title='Sentiment Distribution')
st.plotly_chart(fig_pie)

# Calculate tweet counts by airlines
st.subheader("Tweet Count by Airline")
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

# Create a bar graph using seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='airline', y='count', data=airline_counts, palette='viridis', ax=ax)
ax.set_xlabel('Airline')
ax.set_ylabel('Tweet Count')
ax.set_title('Tweet Count by Airline')
st.pyplot(fig)
