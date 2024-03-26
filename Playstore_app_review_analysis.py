import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('Training_Data_Google_Play_reviews_6000.xlsx')

# Objective 1: Determine the distribution of scores
plt.figure(figsize=(8, 5))
sns.countplot(x='score', data=df)
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Count')
plt.show()

# Objective 2: Explore the relationship between score and thumbs up count
plt.figure(figsize=(8, 6))
sns.scatterplot(x='score', y='thumbsUpCount', data=df)
plt.title('Relationship between Score and Thumbs Up Count')
plt.xlabel('Score')
plt.ylabel('Thumbs Up Count')
plt.show()

# Objective 3: Identify the top languages used for reviews
plt.figure(figsize=(10, 6))
top_lang = df['userLang'].value_counts().head(10)
sns.barplot(x=top_lang.index, y=top_lang.values)
plt.title('Top 10 Languages Used for Reviews')
plt.xlabel('Language')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=45)
plt.show()

# Objective 4: Analyze the frequency of reviews over time
df['at'] = pd.to_datetime(df['at'])
plt.figure(figsize=(10, 6))
df['at'].dt.month.value_counts().sort_index().plot(kind='bar')
plt.title('Frequency of Reviews Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=45)
plt.show()

# Objective 5: Investigate sentiment differences between app versions
plt.figure(figsize=(10, 6))
sns.boxplot(x='reviewCreatedVersion', y='score', data=df)
plt.title('Sentiment Differences Between App Versions')
plt.xlabel('App Version')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.show()

# Objective 6: Explore developer reply rate and content
reply_count = df['replyContent'].notnull().sum()
total_reviews = len(df)
reply_rate = (reply_count / total_reviews) * 100
print(f"Developer Reply Rate: {reply_rate:.2f}%")