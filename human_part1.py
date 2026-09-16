"""
Part 1: basic rating statistics.

    uv run python human_part1.py

Answer the four questions below with your own code, print each answer under its label, and
explain each in one sentence in WRITEUP.md.
"""

from load_data import load_all


def human_part1(ratings, ratings_df, movies, movies_df, users, users_df):


    print("== (a) ==")
    # (a) How many ratings, users, and movies are there, and how are ratings distributed across 1-5 stars?
    print(len(ratings_df))
    print(len(users_df))
    print(len(users_df))
    ratings_dist = ratings_df['rating'].value_counts().sort_index()
    print("Distribution")
    print(ratings_dist)
    print("== (b) ==")
    # (b) What is the median number of ratings per user, and how many users have 100 or more ratings?
    ratings_per_user = ratings_df['user_id'].value_counts()
    median_rpu = ratings_per_user.median()
    
    user100 = (ratings_per_user >= 100).sum()
    
    print("Median ratings per user:")
    print(median_rpu)
    print("Users with >= 100 ratings:")
    print(user100)
    


    print("== (c) ==")
    # (c) Join ratings to titles. Which 10 movies have the most ratings?
    ratings_titles = ratings_df.merge(movies_df[['movie_id', 'title']], on='movie_id')
    best10 = ratings_titles.sort_values('rating', ascending=False).head(11)
    
    print(best10[['user_id', 'title', 'rating']])
    
    print("== (d) ==")
    # (d) Among movies with at least 20 ratings, which 10 have the highest mean rating?
    #     Show title, mean, and count.
    stats = ratings_titles.groupby('title')['rating'].agg(['mean', 'count'])
    stats = stats[stats['count'] >= 20]
    print(stats.sort_values('mean', ascending=False).head(10))


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part1(ratings, ratings_df, movies, movies_df, users, users_df)
