import math
from collections import defaultdict

def find_best_bar(f):
    d = {} #create dict
    barlist = [] #create list
    for lines in open(f): #reads file
        name, rating, curropp, maxopp = lines.split("|") 
        safety = ((1 - (float(curropp)/float(maxopp)))*100)#Math starts
        coolness = ((float(curropp)/float(maxopp))*100)*float(rating)/5
        stats = (safety+coolness)/2 # math ends here
        barlist.append((name, stats)) #appends to list tuples of (name, stats)
    d = dict(barlist) #turns list of tuples into dictionary
    return d #returns dictionary
    
# KEY NOTE !!!!!!! in the test file, the data MUST be in form: name|rating|currentpop|maxpop
# else, the code will not work. Currently, the test data given is not in this form. If this is an issue I(shawn) will make it able to work if possible.

def main():
    print(find_best_bar("sprintTest.txt"))
main()

