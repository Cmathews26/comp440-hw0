"""
Claude's answers to the three questions in questions.md.

    uv run python claude_answers_1_2_3.py

Filled in by a Claude that has never seen the student's work. Kept as it was written.
"""

from load_data import load_all

MIN_RATINGS = 20  # threshold for "enough ratings to trust the average" in Q1d, Q2, Q3


def question_1(ratings_df, movies_df):
    print("=" * 70)
    print("1(a) Basic counts and rating distribution")
    print("=" * 70)
    n_ratings = len(ratings_df)
    n_users = ratings_df["user_id"].nunique()
    n_movies = ratings_df["movie_id"].nunique()
    print(f"{n_ratings:,} ratings, {n_users:,} users, {n_movies:,} movies")

    counts = ratings_df["rating"].value_counts().sort_index()
    for stars, n in counts.items():
        pct = 100 * n / n_ratings
        print(f"  {stars} star{'s' if stars != 1 else ' '}: {n:>6,}  ({pct:5.1f}%)")

    print()
    print("=" * 70)
    print("1(b) Ratings per user")
    print("=" * 70)
    per_user = ratings_df.groupby("user_id").size()
    print(f"Median ratings per user: {per_user.median():.1f}")
    n_prolific = (per_user >= 100).sum()
    print(f"Users with 100+ ratings: {n_prolific} of {n_users} ({100 * n_prolific / n_users:.1f}%)")

    print()
    print("=" * 70)
    print("1(c) 10 most-rated movies")
    print("=" * 70)
    joined = ratings_df.merge(movies_df[["movie_id", "title"]], on="movie_id")
    most_rated = joined.groupby("title").size().sort_values(ascending=False).head(10)
    for title, n in most_rated.items():
        print(f"  {n:>4}  {title}")

    print()
    print("=" * 70)
    print(f"1(d) Highest mean rating among movies with >= {MIN_RATINGS} ratings")
    print("=" * 70)
    stats = joined.groupby("title")["rating"].agg(mean="mean", count="count")
    top_mean = stats[stats["count"] >= MIN_RATINGS].sort_values("mean", ascending=False).head(10)
    for title, row in top_mean.iterrows():
        print(f"  {row['mean']:.3f}  ({row['count']:>3} ratings)  {title}")

    return joined, stats


def bayesian_average(stats, min_ratings, prior_mean):
    """IMDB-style weighted rating: pulls low-count movies toward the global mean so a
    single 5-star rating can't outrank a movie with hundreds of consistently good ones."""
    m = min_ratings
    C = prior_mean
    v = stats["count"]
    R = stats["mean"]
    return (v / (v + m)) * R + (m / (v + m)) * C


def question_2(stats):
    print()
    print("=" * 70)
    print("2. What is the best movie in this dataset?")
    print("=" * 70)
    print(
        "A raw highest-average would be won by a movie with a handful of 5-star ratings.\n"
        "Instead, rank by a Bayesian-weighted average (like IMDB's old Top 250 formula):\n"
        "each movie's mean is pulled toward the global mean, in proportion to how few\n"
        f"ratings it has (using m={MIN_RATINGS} as the pull strength). This rewards movies\n"
        "that are both well-liked AND widely and consistently rated.\n"
    )
    global_mean = stats["mean"].mul(stats["count"]).sum() / stats["count"].sum()
    weighted = bayesian_average(stats, MIN_RATINGS, global_mean).sort_values(ascending=False)
    best_title = weighted.index[0]
    print(f"Global mean rating: {global_mean:.3f}")
    print("\nTop 10 by weighted score:")
    for title, score in weighted.head(10).items():
        row = stats.loc[title]
        print(f"  {score:.3f}  (raw mean {row['mean']:.3f}, {row['count']:>3} ratings)  {title}")
    print(f"\n==> Best movie: {best_title!r}")


def question_3(stats):
    print()
    print("=" * 70)
    print("3. Which movie is the most Unwatchable?")
    print("=" * 70)
    print(
        "Same logic in reverse: the worst movie by raw mean would just be whichever\n"
        f"movie with only 1-2 ratings got unlucky. Restricting to movies with >= {MIN_RATINGS}\n"
        "ratings (so the verdict reflects a real audience, not noise) and taking the lowest\n"
        "Bayesian-weighted score identifies the movie that consistently disappointed a lot\n"
        "of people who bothered to watch it.\n"
    )
    global_mean = stats["mean"].mul(stats["count"]).sum() / stats["count"].sum()
    enough = stats[stats["count"] >= MIN_RATINGS]
    weighted = bayesian_average(enough, MIN_RATINGS, global_mean).sort_values(ascending=True)
    worst_title = weighted.index[0]
    print(f"Bottom 10 by weighted score (>= {MIN_RATINGS} ratings):")
    for title, score in weighted.head(10).items():
        row = stats.loc[title]
        print(f"  {score:.3f}  (raw mean {row['mean']:.3f}, {row['count']:>3} ratings)  {title}")
    print(f"\n==> Most Unwatchable movie: {worst_title!r}")


def claude_answers():
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    joined, stats = question_1(ratings_df, movies_df)
    question_2(stats)
    question_3(stats)


if __name__ == "__main__":
    claude_answers()
