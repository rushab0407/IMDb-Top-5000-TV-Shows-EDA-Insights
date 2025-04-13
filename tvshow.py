# imdb_tv_show_eda.py or notebooks/eda_visualizations.ipynb

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
df = pd.read_csv("/Users/rushabarram/Documents/imdb_top_5000_tv_shows.csv")

# Basic info
print(df.info())
print(df.describe())

# Null value check
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing endYears for ongoing shows
df['endYear'].fillna(2025, inplace=True)  # assuming ongoing if NaN

# Duration of shows
df['duration'] = df['endYear'] - df['startYear']

# ---------------------------------------
# 📊 Visualizations
# ---------------------------------------

# 1. Top Genres
plt.figure(figsize=(10, 5))
df['genres'].str.split(', ').explode().value_counts().head(15).plot(kind='barh', color='skyblue')
plt.title("Top Genres in IMDb Top 5000 TV Shows")
plt.xlabel("Count")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 2. Rating Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['averageRating'], bins=20, kde=True, color='coral')
plt.title("Distribution of IMDb Ratings")
plt.xlabel("Average Rating")
plt.tight_layout()
plt.show()

# 3. Votes vs Ratings Scatter Plot
fig = px.scatter(df, x='numVotes', y='averageRating',
                 size='averageRating', color='genres',
                 hover_name='primaryTitle',
                 title="Votes vs Ratings (Colored by Genre)",
                 size_max=10)
fig.show()

# 4. Shows Over Time
plt.figure(figsize=(12, 5))
sns.countplot(data=df, x='startYear', palette='viridis', order=df['startYear'].value_counts().sort_index().index)
plt.xticks(rotation=90)
plt.title("Number of Shows Released Each Year")
plt.tight_layout()
plt.show()

# 5. Duration of Shows
plt.figure(figsize=(8, 4))
sns.histplot(df['duration'], bins=30, color='mediumseagreen')
plt.title("Show Duration Distribution")
plt.xlabel("Number of Years Aired")
plt.tight_layout()
plt.show()

# 6. Top Rated Shows
top_shows = df.sort_values(by='averageRating', ascending=False).head(10)
print("\n🎬 Top 10 Rated Shows:")
print(top_shows[['primaryTitle', 'averageRating', 'numVotes', 'genres']])
