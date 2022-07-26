import math
from collections import defaultdict

def find_best_bar(f):
    d = {} #create dict
    barlist = [] #create list
    for lines in open(f): #reads file
        name, rating, currpop, maxpop = lines.strip("  ").split("|") #read as file, stripping extra spaces
        rating = float(rating) #make strings into floats
        currpop = float(currpop)
        maxpop =  float(maxpop)
        popularity = (currpop / maxpop) * 100 #math
        safety = (1-(currpop/maxpop))*100
        if (safety == 0):
            score = 0
        elif( popularity == 0):
            score = rating * 4
        elif (safety <= 25):
            score = (rating/5)*safety
        elif (safety > 25 and safety <= 40): #ideal safety threshold
            score = (rating/5)*100
        elif (safety > 40):
            score = ((rating/5)*popularity)
        barlist.append((name, score)) #appends to list tuples of (name, stats)
    barlist = sorted(barlist, key= lambda x: x[1], reverse=True)[:20] #sorts, then picks top 20 stats
    d = dict(barlist) #turns list of tuples into dictionary
    return d #returns dictionary

def main():
    print(find_best_bar("sprintTest2.txt"))
main()
