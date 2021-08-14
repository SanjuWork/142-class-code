import pandas as pd
import numpy as np

df = pd.read_csv('final.csv')

C = df['vote_average'].mean()
m = df['vote_count'].quantile(0.9)
q_movies = df.copy().loc[df['vote_count'] >= m]


##Calculate the values of C, m and find the movies that have more votes than
#0.9 quantile of the movie, just like how we did in Google Colab.

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)

output = q_movies[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(20).values.tolist()

##Explanation of code - 
#Define a function to calculate the weighted rating and create a new
#column of score in the dataframe for all the movies. Create a variable with
#top 20 movies as a list.
