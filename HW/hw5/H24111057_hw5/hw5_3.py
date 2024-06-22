""" 
author: H24111057 姚博瀚
"""

import pandas as pd

# Load the IMDB movie data from the provided CSV file
df = pd.read_csv('/Users/yaohank/Library/CloudStorage/OneDrive-gs.ncku.edu.tw/計算機概論2/HW/hw5/IMDB-Movie-Data.csv')

# 1. Top-3 movies with the highest ratings in 2016
def top_3_highest_ratings_2016(df):
    # Filter the dataframe for movies released in 2016
    df_2016 = df[df['Year'] == 2016]
    # Get the top 3 movies with the highest ratings
    top_3_movies = df_2016.nlargest(3, 'Rating')[['Title', 'Rating']]
    return top_3_movies

# 2. The director who involves in the most movies
def director_most_movies(df):
    # Count the number of movies each director has directed
    director_count = df['Director'].value_counts()
    # Get the director with the most movies
    top_director = director_count.idxmax()
    return top_director, director_count[top_director]

# 3. The actor generating the highest total revenue
def actor_highest_total_revenue(df):
    # Create a dictionary to store the total revenue for each actor
    actors_revenue = {}
    for i, row in df.iterrows():
        revenue = row['Revenue (Millions)']
        # Only consider rows with a valid revenue
        if pd.notna(revenue):
            for actor in row['Actors'].split('| '):
                if actor in actors_revenue:
                    actors_revenue[actor] += revenue
                else:
                    actors_revenue[actor] = revenue
    # Find the actor with the highest total revenue
    top_actor = max(actors_revenue, key=actors_revenue.get)
    return top_actor, actors_revenue[top_actor]

# 4. The average rating of Emma Watson’s movies
def average_rating_emma_watson(df):
    # Filter the dataframe for movies featuring Emma Watson
    emma_watson_movies = df[df['Actors'].str.contains('Emma Watson')]
    # Calculate the average rating of these movies
    average_rating = emma_watson_movies['Rating'].mean()
    return average_rating

# 5. Top-4 actors playing the most movies
def top_4_actors_most_movies(df):
    # Create a dictionary to count the number of movies for each actor
    actor_movie_count = {}
    for actors in df['Actors']:
        for actor in actors.split('| '):
            if actor in actor_movie_count:
                actor_movie_count[actor] += 1
            else:
                actor_movie_count[actor] = 1
    # Get the top 4 actors with the most movies
    top_4_actors = sorted(actor_movie_count.items(), key=lambda x: x[1], reverse=True)[:4]
    return top_4_actors

# 6. Top-7 frequent collaboration pairs of director & actor
def top_7_collaboration_pairs(df):
    # Create a dictionary to count the number of collaborations between each director-actor pair
    director_actor_pairs = {}
    for i, row in df.iterrows():
        director = row['Director']
        actors = row['Actors'].split('| ')
        for actor in actors:
            pair = (director, actor)
            if pair in director_actor_pairs:
                director_actor_pairs[pair] += 1
            else:
                director_actor_pairs[pair] = 1
    # Get the top 7 most frequent collaboration pairs
    top_7_pairs = sorted(director_actor_pairs.items(), key=lambda x: x[1], reverse=True)[:7]
    return top_7_pairs

# 7. Top-3 directors who collaborate with the most actors
def top_3_directors_most_actors(df):
    # Create a dictionary to store the unique actors each director has collaborated with
    director_actors = {}
    for i, row in df.iterrows():
        director = row['Director']
        actors = set(row['Actors'].split('| '))
        if director in director_actors:
            director_actors[director].update(actors)
        else:
            director_actors[director] = actors
    # Get the top 3 directors who have collaborated with the most unique actors
    top_3_directors = sorted(director_actors.items(), key=lambda x: len(x[1]), reverse=True)[:3]
    return [(director, len(actors)) for director, actors in top_3_directors]

# 8. Top-6 actors playing in the most genres of movies
def top_6_actors_most_genres(df):
    # Create a dictionary to store the unique genres each actor has played in
    actor_genres = {}
    for i, row in df.iterrows():
        genres = set(row['Genre'].split(', '))
        actors = row['Actors'].split('| ')
        for actor in actors:
            if actor in actor_genres:
                actor_genres[actor].update(genres)
            else:
                actor_genres[actor] = genres
    # Get the top 6 actors who have played in the most unique genres
    top_6_actors = sorted(actor_genres.items(), key=lambda x: len(x[1]), reverse=True)[:6]
    return [(actor, len(genres)) for actor, genres in top_6_actors]

# 9. Top-3 actors whose movies lead to the largest maximum gap of years
def top_3_actors_largest_gap_years(df):
    # Create a dictionary to store the years of movies for each actor
    actor_years = {}
    for i, row in df.iterrows():
        year = row['Year']
        actors = row['Actors'].split('| ')
        for actor in actors:
            if actor in actor_years:
                actor_years[actor].add(year)
            else:
                actor_years[actor] = {year}
    # Calculate the maximum gap of years for each actor
    actor_gaps = {actor: max(years) - min(years) for actor, years in actor_years.items()}
    # Get the top 3 actors with the largest maximum gap of years
    top_3_actors = sorted(actor_gaps.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_3_actors

# Print results for each question
print("1. Top-3 movies with the highest ratings in 2016:")
print(top_3_highest_ratings_2016(df))
print("\n2. The director who involves in the most movies:")
print(director_most_movies(df))
print("\n3. The actor generating the highest total revenue:")
print(actor_highest_total_revenue(df))
print("\n4. The average rating of Emma Watson’s movies:")
print(average_rating_emma_watson(df))
print("\n5. Top-4 actors playing the most movies:")
print(top_4_actors_most_movies(df))
print("\n6. Top-7 frequent collaboration pairs of director & actor:")
print(top_7_collaboration_pairs(df))
print("\n7. Top-3 directors who collaborate with the most actors:")
print(top_3_directors_most_actors(df))
print("\n8. Top-6 actors playing in the most genres of movies:")
print(top_6_actors_most_genres(df))
print("\n9. Top-3 actors whose movies lead to the largest maximum gap of years:")
print(top_3_actors_largest_gap_years(df))


""" Answer:
1. Top-3 movies with the highest ratings in 2016:
             Title  Rating
2           Dangal     8.8
4    Kimi no na wa     8.6
15  Koe no katachi     8.4

2. The director who involves in the most movies:
('Ridley Scott', 8)

3. The actor generating the highest total revenue:
('Robert Downey Jr.', 2739.2899999999995)

4. The average rating of Emma Watson’s movies:
7.175000000000001

5. Top-4 actors playing the most movies:
[('Mark Wahlberg', 15), ('Christian Bale', 13), ('Hugh Jackman', 13), ('Brad Pitt', 13)]

6. Top-7 frequent collaboration pairs of director & actor:
[(('David Yates', 'Daniel Radcliffe'), 4), (('David Yates', 'Emma Watson'), 4), (('David Yates', 'Rupert Grint'), 4), (('Ridley Scott', 'Russell Crowe'), 4), (('Lars von Trier', 'Charlotte Gainsbourg'), 4), (('Dennis Dugan', 'Adam Sandler'), 4), (('Paul W.S. Anderson', 'Milla Jovovich'), 4)]

7. Top-3 directors who collaborate with the most actors:
[('Ridley Scott', 24), ('M. Night Shyamalan', 22), ('Danny Boyle', 19)]

8. Top-6 actors playing in the most genres of movies:
[('Matt Damon', 21), ('Jack Nicholson', 21), ('Mark Wahlberg', 21), ('Matthew McConaughey', 20), ('Anne Hathaway', 20), ('Jessica Chastain', 20)]

9. Top-3 actors whose movies lead to the largest maximum gap of years:
[('Christian Bale', 10), ('Anne Hathaway', 10), ('Hugh Jackman', 10)]
"""