# HW0 writeup

**Name:** Colin Mathews
**Date:** 2026-09-16

Replace every placeholder below with your answer. Every number you give comes from a script in this repo; say which one.

## Part 1. Basic rating statistics

Code: `human_part1.py`. One or two sentences per answer, with the numbers.

**(a) How many ratings, users, and movies are there, and how are ratings distributed across 1–5 stars?**

There are 100000 ratings, 943 movies and 943 users; and the majority of ratings are skewed toward 3 and 4 stars with the lowest number being 1 star reviews

**(b) What is the median number of ratings per user, and how many users have 100 or more ratings?**

The median number of ratings per user is 65.0 and there are 364 users with at least 100 ratings. 

**(c) Which 10 movies have the most ratings?**

0                                                     Kolya (1996)
1                                   L.A. Confidential (1997)
2                                         Heavyweights (1994)
3                                 Legends of the Fall (1994)
4                                        Jackie Brown (1997)
5          Dr. Strangelove or: How I Learned to Stop Worr...
6                           Hunt for Red October, The (1990)
7                                    Jungle Book, The (1994)
8                                              Grease (1978)
9                               Remains of the Day, The (1993) 

**(d) Among movies with at least 20 ratings, which 10 have the highest mean rating?**

Answers are listed under d.

**Anything you got stuck on (what you tried, where it broke), or "none":**

Setup of the homework was the hardest part for me, and then I had to remind myself how to do a couple of df related things in pandas by using the internet because my brain has been working in R. 

## Part 2. The best movie

Code: `human_part2.py`.

**My rule:** Movies with at least 100 ratings and zero 1 star ratings

**One rule I considered and rejected, and why:** Action movies made before the year 2010 with no reviews under 3 stars and over 400 ratings. Rejected due to complication and pandas familiarity. 

**Top 10 under my rule:**
Rear Window
Citizen Kane
Dr Strangelove
Good Will Hunting
Lawrence of Arabia
North by Northwest
Apollo 13
Taxi Driver 
Vertigo 
Young Frankenstein

**Why my rule, in at most 150 words. Name one thing it gains and one thing it loses:**

I think that my rule's biggest strength is also its biggest weakness in that the simple parameters of the rule make the data fairly easy to work with, but the simplicity itself limits the scope through whcih I can view the movies in the dataset. 

## Part 3. The most ___ movie

Code: `human_part3.py`.

**My adjective:** Unwatchable

**My definition** (one sentence, precise enough that a classmate could code it)**:** Movies with >= 35 1 star ratings

**One definition I considered and rejected, and why:** Movies with >=100 1 star ratings- There were no movies in the dataset with that many 1 star ratings 

**Top 5 under my definition:**

Liar Liar
Evita
Crash
Beavis and Butt-head Do America
Jungle2Jungle

**What your definition captures, what it misses, and where "___-ness" lives in this data — the
genre labels, what the crowd did, or the words in the titles. At most 150 words:**

My definition captures I think generally poorly recieved films, but it certainly misses the nuance in an individual's enjoyment of a "bad" movie. I set out to capture what movies were the worst, and the only real pattern/similarity I found between my top (or bottom) 5 was that they were all made in 1996 or 1997. 
## Part 4. Claude's answers

Claude answers the same three questions in `claude_answers_1_2_3.py`, without seeing your code
or your answers.

**Did its numbers for Part 1 match yours? If not, which, and what did you find?**

Yes our numbers matched up. For some reason, the listed movies don't match and I cannot figure out why. 

## Part 5. Comparing the best movie

**Claude's rule:**

Claude ranked by a Bayesian weighted average

**Read what Claude wrote about its rule. Does it anywhere admit the rule was a choice, and that a different rule was possible? Or does it give its answer as simply the answer? Quote the sentence that decides it:**

A raw highest-average would be won by a movie with a handful of 5-star ratings.
Instead, rank by a Bayesian-weighted average (like IMDB's old Top 250 formula):
each movie's mean is pulled toward the global mean, in proportion to how few
ratings it has (using m=20 as the pull strength). This rewards movies
that are both well-liked AND widely and consistently rated.

Claude appears to have considered using just a raw highest average but decided it was too simple and limiting. 

**Your Part 2 top 10 and Claude's Part 2 top 10 — not the Part 1(d) lists. Where do they differ, and why?**

The only similarity in our two lists is Rear Window. They differ everywhere else because Claude used a weighted average and I simply used volume ratings > 3 stars combined with 0 1 star ratings. 

**Better for what purpose? Name a situation where your rule is the right one and a situation where Claude's is. At most 150 words. You may conclude yours, its, or neither:**

Mine would be better for showing "total crowd pleasers," or movies that, at least within the dataset, nobody hated enough to give it a 1 star review. Claude's is better for showing the whole picture as well as relating the top movies with the movies already in the dataset. If you wanted to know in general I think my rule is better but I think working in this context I would probably rather have Claude's rule. 

## Part 6. Comparing the most ___ movie

**Claude's definition:**

the worst movie by raw mean would just be whichever
movie with only 1-2 ratings got unlucky. Restricting to movies with >= 20
ratings (so the verdict reflects a real audience, not noise) and taking the lowest
Bayesian-weighted score identifies the movie that consistently disappointed a lot
of people who bothered to watch it.

**Is Claude's film in your top 5?**

No 

**What Claude's definition sees that yours does not, and the reverse. At most 150 words:**

Claude's definition is pretty similar to mine but mine takes the extreme whereas Claude's tries to find general poor reception. I.e. my rule is only concerned with movies that people thought were the absolute worst whereas Claude's movies could have achieved their low weighted averages through a bunch of 2 and 3 ratings as opposed to 1 star ratings. 

## Working with Claude

**What you asked Claude for during Parts 1–3** (debugging and installing only — say what you
got stuck on)**:**

Just general python syntax that I had forgotten as a Data Science major working in R all the time. 
**Something Claude said that you could not verify, and why. Or "none," and how you checked:**

None

**What you would do differently next time, in 3–5 sentences:**

I would try to get out ahead of Claude and presume what it's going to try to think so I could see how close I could actually get. In this assignment, I just did what I felt like I could do or what I felt like would be best. I wasn't concerned at all with how I thought Claude would do it after me. 

**Where did this assignment slow you down for a reason that was its fault, not yours? Point at
the step. Or "nowhere." One or two sentences:**

Nowhere

**Hours spent:** 4 hours 

**Anyone who helped you, or "no one":** Google, StackOverflow, Adam Lail 
