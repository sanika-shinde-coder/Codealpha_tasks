#IMPORTING NESSARY LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

#Read the data
df=pd.read_csv("amazon_reviews_Dataset.csv")

#Taking only 1000 records for analysis
df=df.head(1000)
print(df.head())

#PLOT bar CHART OF REVIEW STARS VS COUNT OF REVIEW STARS
plt.figure(figsize=(10,5))
rating_count=df['Score'].value_counts().sort_index()
plt.bar(rating_count.index,rating_count.values,color="purple")
plt.title("Number of Reviews by Stars Rating")
plt.xlabel('Star Rating')
plt.ylabel('Number of Reviews')
plt.show()

#Analysing Sentiments 
sia=SentimentIntensityAnalyzer()
res={}
for i,row in tqdm(df.iterrows(),total=len(df)):
    text=row['Text']
    myid=row['ID']
    res[myid]=sia.polarity_scores(text)

vaders=pd.DataFrame(res).T
vaders=vaders. reset_index().rename(columns={'index':'ID'})
vaders=vaders.merge(df,how='left')
print(vaders.head())

# Convert compound score into sentiment label
def get_sentiment(compound):
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

vaders['Sentiment'] = vaders['compound'].apply(get_sentiment)
print(vaders[['compound', 'Sentiment']].head())
sns.countplot(data=vaders, x='Sentiment',color='orange')
plt.title("Sentiment Distribution of Amazon Reviews")
plt.show()

#Draw the pie chart
plt.figure(figsize=(6,6))
sentiment_counts = vaders['Sentiment'].value_counts()
plt.pie(sentiment_counts,labels=sentiment_counts.index,autopct='%1.1f%%')
plt.title("Sentiment Distribution of Amazon Reviews", fontsize=14)
plt.axis('equal')
plt.show()

ax=sns.barplot(data=vaders,x='Score',y='compound')
ax.set_title('Compound Score by Amazon Star Review')
plt.show() 

#comparing positive,negative & neutral reviews
grouped = (
    vaders
    .groupby('Score')[['pos', 'neg', 'neu']]
    .mean()
    .reset_index()
)

x = np.arange(len(grouped['Score']))  # positions for stars
width = 0.25                           # width of each bar

plt.figure(figsize=(8,5))

plt.bar(x - width, grouped['pos'], width, label='Positive')
plt.bar(x,         grouped['neg'], width, label='Negative')
plt.bar(x + width, grouped['neu'], width, label='Neutral')

plt.xticks(x, grouped['Score'])
plt.xlabel("Star Rating")
plt.ylabel("Average Sentiment Score")
plt.title("Sentiment Breakdown by Star Rating")
plt.legend()

plt.tight_layout()
plt.show()


