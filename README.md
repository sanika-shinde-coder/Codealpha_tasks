1.MOBILE SALES ANALYSIS
📌 Project Overview

This project features an interactive Power BI dashboard designed to analyze mobile phone sales data across multiple business dimensions. The goal is to transform raw sales data into meaningful insights that support data-driven decision making.

The dashboard focuses on sales performance, customer behavior, brand analysis, and regional trends, presented through clean visuals and interactive filters.

🎯 Project Objectives

1.Analyze overall mobile sales performance

2.Track key KPIs such as sales, quantity, transactions, and averages

3.Identify top-performing brands and mobile models

4.Understand customer preferences through ratings and payment methods

5.Explore regional sales distribution across cities

🧩 Key Metrics (KPIs)

1.Total Sales

2.Total Quantity Sold

3.Total Transactions

4.Average Sales Value

📈 Dashboard Features

🔹 Sales Analysis
   Monthly sales and quantity trends
   Day-wise sales performance

🔹 Geographic Insights
   City-wise sales distribution using map visualization

🔹 Brand & Product Insights
   Total sales by brand
   Sales comparison across mobile models

🔹 Customer Insights
   Customer ratings distribution
   Analysis of payment methods (UPI, Debit Card, Credit Card, Cash)

🔹 Interactivity
   Dynamic slicers for: 
    Month
    Brand
    Mobile Model
    Payment Method
    Day Name

🛠 Tools & Technologies Used

   Power BI – Data modeling, DAX, dashboard creation
   
   Microsoft Excel – Data cleaning and preprocessing




2.SENTIMENT ANALYSIS
📌 Project Overview

This project performs sentiment analysis on Amazon product reviews to understand customer opinions and sentiment trends. Using Natural Language Processing (NLP) techniques and the VADER sentiment lexicon, reviews are classified into Positive, Negative, and Neutral categories. The results are visualized using multiple charts to derive meaningful insights.

🎯 Objectives

Classify customer reviews into Positive, Negative, and Neutral sentiments

Analyze sentiment trends across different star ratings

Visualize sentiment distribution and review patterns

Gain insights into customer behavior and public opinion

🗂 Dataset

Source: Amazon Reviews Dataset

Records Used: First 1000 reviews (for efficient analysis)

Key Columns:

Text – Customer review text

Score – Star rating (1 to 5)

ID – Unique review identifier

🛠 Technologies & Libraries Used

Python

Pandas & NumPy – Data manipulation

Matplotlib & Seaborn – Data visualization

NLTK – Natural Language Processing

VADER SentimentIntensityAnalyzer – Sentiment scoring

🔍 Methodology

Loaded and explored the Amazon reviews dataset

Applied VADER Sentiment Analyzer to calculate sentiment scores

Classified reviews based on compound score thresholds:

compound ≥ 0.05 → Positive

compound ≤ -0.05 → Negative

Otherwise → Neutral

Created visualizations to analyze:

Review count by star rating

Overall sentiment distribution

Sentiment percentage breakdown

Sentiment trends across star ratings

📊 Visualizations Included

⭐ Number of Reviews by Star Rating (Bar Chart)

😊 Sentiment Distribution (Bar Chart & Pie Chart)

📈 Compound Sentiment Score by Star Rating

📊 Positive, Negative & Neutral Sentiment Comparison by Rating

📈 Key Insights

Majority of reviews are positive, indicating strong customer satisfaction

Higher star ratings correlate with higher positive sentiment scores

Negative sentiment decreases as star ratings increase

Neutral sentiment remains relatively consistent across ratings
