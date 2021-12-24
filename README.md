# SWA_Hateful_USER
The link to a zip file for the data used in this project is here: https://drive.google.com/file/d/1ZmZ5lObD8pJ6bz4sN22pGUnv_t4MP6MP/view?usp=sharing

# Context
This dataset contains a network of 100k users, out of which ~5k were annotated as hateful or not.
For each user, several content-related, network-related and activity related features were provided.

# Content
users_anon_neighborhood.csv file with several features for each user as well as the avg for some features for their 1-neighborhood (ppl they tweeted). Notice that c_ are attributes calculated for the 1-neighborhood of a user in the retweet network (averaged out).

# Attributes description
  hate :("hateful"|"normal"|"other")
  if user was annotated as hateful, normal, or not annotated.

  (is_50|is_50_2) :bool
  whether user was deleted up to 12/12/17 or 14/01/18. 

  (is_63|is_63_2) :bool
  whether user was suspended up to 12/12/17 or 14/01/18. 

  (hate|normal)_neigh :bool
  is the user on the neighborhood of a (hateful|normal) user? 

  [c_] (statuses|follower|followees|favorites)_count :int
  number of (tweets|follower|followees|favorites) a user has.

  [c_] listed_count:int
  number of lists a user is in.

  [c_] (betweenness|eigenvector|in_degree|outdegree) :float
  centrality measurements for each user in the retweet graph.

  [c_] *_empath :float
  occurrences of empath categories in the users latest 200 tweets.

  [c_] *_glove :float          
  glove vector calculated for users latest 200 tweets.

  [c_] (sentiment|subjectivity) :float
  average sentiment and subjectivity of users tweets.

  [c_] (time_diff|time_diff_median) :float
  average and median time difference between tweets.

  [c_] (tweet|retweet|quote) number :float
  percentage of direct tweets, retweets and quotes of an user.

  [c_] (number urls|number hashtags|baddies|mentions) :float
  number of bad words|mentions|urls|hashtags per tweet in average.

  [c_] status length :float
  average status length.

  hashtags :string
  all hashtags employed by the user separated by spaces.
