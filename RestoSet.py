import os
import csv
import sys
import re

from surprise import Dataset
from surprise import Reader

from collections import defaultdict
import numpy as np

class RestoSet:

    restoID_to_name = {}
    name_to_restoID = {}
    ratingsPath = '../ml-latest-small/dataasli.csv' #ratingdataset.csv ,ratingdataset2.csv, dataasli.csv
    restoPath = '../ml-latest-small/resto_dataset3.csv' #restodataset.csv, resto_dataset3.csv
    
    def loadRestoSetLatestSmall(self):

        # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))

        ratingsDataset = 0
        self.restoID_to_name = {}
        self.name_to_restoID = {}

        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)

        ratingsDataset = Dataset.load_from_file(self.ratingsPath, reader=reader)

        with open(self.restoPath, newline='', encoding='ISO-8859-1') as csvfile:
                restoReader = csv.reader(csvfile)
                next(restoReader)  #Skip header line
                for row in restoReader:
                    restoID = int(row[0])
                    restoName = row[1]
                    self.restoID_to_name[restoID] = restoName
                    self.name_to_restoID[restoName] = restoID
        return ratingsDataset

    def getUserRatings(self, user):
        userRatings = []
        hitUser = False
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                if (user == userID):
                    restoID = int(row[1])
                    rating = float(row[2])
                    userRatings.append((restoID, rating))
                    hitUser = True
                if (hitUser and (user != userID)):
                    break

        return userRatings

    def getPopularityRanks(self):
        ratings = defaultdict(int)
        rankings = defaultdict(int)
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                restoID = int(row[1])
                ratings[restoID] += 1
        rank = 1
        for restoID, ratingCount in sorted(ratings.items(), key=lambda x: x[1], reverse=True):
            rankings[restoID] = rank
            rank += 1
        return rankings
    
    def getCuisine(self):
        cuisine = defaultdict(list)
        cuisineIDs = {}
        maxCuisineID = 0
        with open(self.restoPath, newline='', encoding='ISO-8859-1') as csvfile:
            restoReader = csv.reader(csvfile)
            next(restoReader)  #Skip header line
            for row in restoReader:
                restoID = int(row[0])
                cuisineList = row[2].split('|')
                cuisineIDList = []
                for cuisine in cuisineList:
                    if cuisine in cuisineIDs:
                        cuisineID = cuisineIDs[cuisine]
                    else:
                        cuisineID = maxCuisineID
                        cuisineIDs[cuisine] = cuisineID
                        maxCuisineID += 1
                    cuisineIDList.append(cuisineID)
                cuisine[restoID] = cuisineIDList
        # Convert integer-encoded genre lists to bitfields that we can treat as vectors
        for (restoID, cuisineIDList) in cuisine.items():
            bitfield = [0] * maxCuisineID
            for cuisineID in cuisineIDList:
                bitfield[cuisineID] = 1
            cuisine[restoID] = bitfield            
        
        return cuisine
    
#    def getYears(self):
#        p = re.compile(r"(?:\((\d{4})\))?\s*$")
#        years = defaultdict(int)
#        with open(self.moviesPath, newline='', encoding='ISO-8859-1') as csvfile:
#            movieReader = csv.reader(csvfile)
#            next(movieReader)
#            for row in movieReader:
#                movieID = int(row[0])
#                title = row[1]
#                m = p.search(title)
#                year = m.group(1)
#                if year:
#                    years[movieID] = int(year)
#        return years
    
    def getMiseEnScene(self):
        mes = defaultdict(list)
        with open("LLVisualFeatures13K_Log.csv", newline='') as csvfile:
            mesReader = csv.reader(csvfile)
            next(mesReader)
            for row in mesReader:
                restoID = int(row[0])
                avgShotLength = float(row[1])
                meanColorVariance = float(row[2])
                stddevColorVariance = float(row[3])
                meanMotion = float(row[4])
                stddevMotion = float(row[5])
                meanLightingKey = float(row[6])
                numShots = float(row[7])
                mes[restoID] = [avgShotLength, meanColorVariance, stddevColorVariance,
                   meanMotion, stddevMotion, meanLightingKey, numShots]
        return mes
    
    def getRestoName(self, restoID):
        if restoID in self.restoID_to_name:
            return self.restoID_to_name[restoID]
        else:
            return ""
        
    def getRestoID(self, restoName):
        if restoName in self.name_to_restoID:
            return self.name_to_restoID[restoName]
        else:
            return 0