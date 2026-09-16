"""
Part 2: the best movie.

    uv run python human_part2.py

Write your rule on the `**My rule:**` line of WRITEUP.md. Print the top 10 movies (id, title,
ratings count, mean rating) under it.
"""

from load_data import load_all


def top10_my_rule(ratings, ratings_df, movies, movies_df):
    print("== My rule ==")
    stats = ratings_df.groupby('movie_id')['rating'].agg(
        count='count',
        one_star=lambda x: (x == 1).sum(),
        five_star=lambda x: (x == 5).sum(),
        mean='mean'
        )

    result = stats[(stats['count'] >= 100) & (stats['one_star'] == 0)]
    top10 = result.sort_values('five_star', ascending=False).head(10)
    top10 = top10.merge(movies_df[['movie_id', 'title']], on='movie_id')

    print(top10[['movie_id', 'title', 'count', 'mean']])

def human_part2(ratings, ratings_df, movies, movies_df):
    top10_my_rule(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part2(ratings, ratings_df, movies, movies_df)
