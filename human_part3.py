"""
Part 3: the most ___ movie.

    uv run python human_part3.py

Pick an adjective. Write it on the `**My adjective:**` line of WRITEUP.md and a one-sentence
definition a classmate could code on the `**My definition:**` line. Print the top 5 movies
under it.
"""

from load_data import load_all


def top5_my_definition(ratings, ratings_df, movies, movies_df):
    print("== My definition ==")
    stats = ratings_df.groupby('movie_id')['rating'].agg(
        count='count',
        one_star=lambda x: (x == 1).sum(),
        mean='mean'
    )

    result = stats[stats['one_star'] >= 35]
    top5 = result.sort_values('one_star', ascending=False).head(5)
    top5 = top5.merge(movies_df[['movie_id', 'title']], on='movie_id')

    print(top5[['movie_id', 'title', 'count', 'one_star', 'mean']])

def human_part3(ratings, ratings_df, movies, movies_df):
    top5_my_definition(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part3(ratings, ratings_df, movies, movies_df)
