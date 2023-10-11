from RestoSet import RestoSet
from surprise import SVD
from surprise import KNNBaseline
from surprise.model_selection import train_test_split
from surprise.model_selection import LeaveOneOut
from RecommenderMetrics import RecommenderMetrics

rs = RestoSet()

print("Loading resto ratings...")
data = rs.loadRestoSetLatestSmall()

print("\nComputing resto popularity ranks so we can measure novelty later...")
rankings = rs.getPopularityRanks()

print("\nComputing item similarities so we can measure diversity later...")
fullTrainSet = data.build_full_trainset()
sim_options = {'name': 'cosine', 'user_based': True} #pearson_baseline
simsAlgo = KNNBaseline(sim_options=sim_options)
simsAlgo.fit(fullTrainSet)

print("\nBuilding recommendation model...")
trainSet, testSet = train_test_split(data, test_size=.30, random_state=1)

algo = SVD(random_state=10)
algo.fit(trainSet)

print("\nComputing recommendations...")
predictions = algo.test(testSet)

print("\nEvaluating accuracy of model...")
print("RMSE: ", RecommenderMetrics.RMSE(predictions))
print("MAE: ", RecommenderMetrics.MAE(predictions))

print("\nEvaluating top-10 recommendations...")

# Set aside one rating per user for testing
LOOCV = LeaveOneOut(n_splits=1, random_state=1)

for trainSet, testSet in LOOCV.split(data):
    print("Computing recommendations with leave-one-out...")

    # Train model without left-out ratings
    algo.fit(trainSet)

    # Predicts ratings for left-out ratings only
    print("Predict ratings for left-out set...")
    leftOutPredictions = algo.test(testSet)

    # Build predictions for all ratings not in the training set
    print("Predict all missing ratings...")
    bigTestSet = trainSet.build_anti_testset()
    allPredictions = algo.test(bigTestSet)

    # Compute top 10 recs for each user
    print("Compute top 10 recs per user...")
    topNPredicted = RecommenderMetrics.GetTopN(allPredictions, n=10)

    # See how often we recommended a movie the user actually rated
    print("\nHit Rate: ", RecommenderMetrics.HitRate(topNPredicted, leftOutPredictions))

    # Break down hit rate by rating value
    print("\nrHR (Hit Rate by Rating value): ")
    RecommenderMetrics.RatingHitRate(topNPredicted, leftOutPredictions)

    # See how often we recommended a movie the user actually liked (ASLINYA 4)
    print("\ncHR (Cumulative Hit Rate, rating >= 2): ", RecommenderMetrics.CumulativeHitRate(topNPredicted, leftOutPredictions, 2.0))

    # Compute ARHR
    print("\nARHR (Average Reciprocal Hit Rank): ", RecommenderMetrics.AverageReciprocalHitRank(topNPredicted, leftOutPredictions))

print("\nComputing complete recommendations, no hold outs...")
algo.fit(fullTrainSet)
bigTestSet = fullTrainSet.build_anti_testset()
allPredictions = algo.test(bigTestSet)
topNPredicted = RecommenderMetrics.GetTopN(allPredictions, n=10)

# Print user coverage with a minimum predicted rating of 4.0: (aslinya 4.0)
print("\nUser coverage: ", RecommenderMetrics.UserCoverage(topNPredicted, fullTrainSet.n_users, ratingThreshold=2.0))

# Measure diversity of recommendations:
print("\nDiversity: ", RecommenderMetrics.Diversity(topNPredicted, simsAlgo))

# Measure novelty (average popularity rank of recommendations):
print("\nNovelty (average popularity rank): ", RecommenderMetrics.Novelty(topNPredicted, rankings))