#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import requests
from bs4 import BeautifulSoup

import re
import time


# In[2]:


link = pd.read_csv("links.csv")
movie = pd.read_csv("movies.csv")
rating = pd.read_csv("ratings.csv")
tag = pd.read_csv("tags.csv")


# In[46]:


#What is the shape of "movies.csv"?
movie.shape


# In[47]:


#What is the shape of "ratings.csv"?
rating.shape


# In[48]:


#How many unique "userId" are available in "ratings.csv"?
rating['userId'].nunique()


# In[6]:


# Merging link and movie on 'movieId'
merged_table = pd.merge(link, movie, on='movieId')

# Merging the result with rating on 'movieId'
merged_table = pd.merge(merged_table, rating, on='movieId')

# Merging the result with tag on 'movieId'
merged_table = pd.merge(merged_table, tag, on='movieId')


# In[7]:


merged_table


# In[8]:


import pickle
with open('imdb.pkl','wb') as f:
        pickle.dump(merged_table,f)


# In[9]:


with open('imdb.pkl','rb') as f:
    df=pickle.load(f)


# In[10]:


df


# In[11]:


movie_rating_counts = df.groupby('title')['userId_x'].nunique()


# In[12]:


movie_rating_counts 


# In[13]:


df.groupby(['userId_x','rating'])['title'].max().sort_values(ascending=False)


# In[16]:


df.groupby('title')['rating'].max().sort_values(ascending=False)


# In[49]:


#Which movie has recieved maximum number of user ratings?
df.groupby('title')['userId_x'].count().idxmax()


# In[18]:


ratings_count = df.groupby('movieId')['rating'].count()


# In[19]:


ratings_count


# In[20]:


max_ratings_movie = ratings_count.idxmax()


# In[21]:


max_ratings_movie 


# In[50]:


#Select all the correct tags submitted by users to "Matrix, The (1999)" movie?

matrix_tags = df.loc[df['title'] == 'Matrix, The (1999)', 'tag']


# In[51]:


matrix_tags.nunique()


# In[52]:


matrix_tags


# In[25]:


#What is the average user rating for movie named "Terminator 2: Judgment Day (1991)"?

t2_ratings = df.loc[df['title'] == 'Terminator 2: Judgment Day (1991)', 'rating']

# Calculating the average rating
avg_rating = t2_ratings.mean()


# In[26]:


avg_rating


# In[53]:


#How does the data distribution of user ratings for "Fight Club (1999)" movie looks like?

# Filter the DataFrame to include only the ratings for "Fight Club (1999)"
FC = df.loc[df['title'] == 'Fight Club (1999)', 'rating']

# Plot the data distribution
plt.hist(FC , bins=10, edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Data Distribution of User Ratings for "Fight Club (1999)"')
plt.show()


# ## Left-skewed distribution

# In[ ]:





# Mandatory Operations:
# 1. Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings. 
# 2. Apply inner join on dataframe created from movies.csv and the grouped df from step 1.
# 3. Filter only those movies which have more than 50 user ratings (i.e. > 50).
# 
# Above steps will make sure that your data contains only those movies which has recieved more than 50 user ratings.
# 

# In[28]:


# Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings
movie_ratings = df.groupby('movieId')['rating'].agg(['count', 'mean']).reset_index()


# In[29]:


movie_ratings


# In[30]:


# Apply inner join on dataframe created from movies.csv and the grouped df from step 1
merged_df = pd.merge(movie, movie_ratings, on='movieId', how='inner')


# In[31]:


merged_df


# In[32]:


# Filter only those movies which have more than 50 user ratings (i.e. > 50)
popular_movies = merged_df[merged_df['count'] > 50]


# In[33]:


popular_movies


# In[34]:


#Which movie is the most popular based on  average user ratings?

most_popular_movie = popular_movies.loc[popular_movies['mean'].idxmax(), 'title']


# In[35]:


most_popular_movie


# In[36]:


merged_df


# In[38]:


#Which Sci-Fi movie is "third most popular" based on the number of user ratings?


# Filter the DataFrame to include only the Sci-Fi movies
scifi_movies = df[df['genres'].str.contains('Sci-Fi')]

# Group the user ratings based on movieId and applying aggregation operations 
movie_ratings = df.groupby('movieId')['rating'].agg(['count', 'mean']).reset_index()

# inner join on dataframe
merged_df = pd.merge(scifi_movies, movie_ratings, on='movieId', how='inner')

# Sort the movies by number of user ratings in descending order
sorted_movies = merged_df.sort_values(by='count', ascending=False)

# Select the third most popular movie
third_most_popular_movie = sorted_movies.iloc[2]['title']


# In[39]:


third_most_popular_movie


# In[42]:


#write a python code for Mention the movieId of the movie which has the highest IMDB rating.

# Find the row with the highest IMDb rating
highest_rated_movie = df.loc[df['imdbId'].idxmax()]

print(f"The movieId of the movie with the highest IMDb rating is {highest_rated_movie['movieId']}.")


# In[43]:


df.iloc[180031]


# In[44]:


#Mention the movieId of the "Sci-Fi" movie which has the highest IMDB rating.

# Filter the DataFrame to include only the Sci-Fi movies
scifi_movies = df[df['genres'].str.contains('Sci-Fi')]

# Find the row with the highest IMDb rating
highest_rated_scifi_movie = scifi_movies.loc[scifi_movies['imdbId'].idxmax()]

print(f"The movieId of the Sci-Fi movie with the highest IMDb rating is {highest_rated_scifi_movie['movieId']}.")


# In[45]:


df.iloc[187593]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


df.columns


# In[ ]:





# In[ ]:





# In[ ]:


ipl_ball.groupby(['batsman','non_striker'])['batsman_runs'].sum().sort_values(ascending=False)


# In[ ]:





# In[ ]:





# In[ ]:


df


# In[ ]:





# In[ ]:




