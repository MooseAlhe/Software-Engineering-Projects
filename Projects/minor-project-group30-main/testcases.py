import random
f = open('restaurant-names.txt')
names = []
for i in f:
    names.append(i.strip())
def randomNames(number):
    indices = random.sample(range(len(names)), number)
    return [names[index] for index in indices]
f.close()

testcases = []
temp = randomNames(300)
### Unsafe Bars
for i in range(50):
    rating = round(random.uniform(1, 5),2)
    totalOccupants = random.randint(100, 1000)
    currentOccupants = random.randint(round(totalOccupants*0.9), totalOccupants)
    print(temp[i] , " | " , rating , " | " , currentOccupants ,  " | " , totalOccupants)
### High Rating + Low Occupancy
for i in range(50, 100):
    rating = round(random.uniform(4, 5),2)
    totalOccupants = random.randint(100, 1000)
    currentOccupants = random.randint(0, round(totalOccupants*0.10))
    print(temp[i] , " | " , rating , " | " , currentOccupants ,  " | " , totalOccupants)
### Low Rating + High Safe Occupancy
for i in range(100, 150):
    rating = round(random.uniform(1, 2),2)
    totalOccupants = random.randint(100, 1000)
    currentOccupants = random.randint(round(totalOccupants*0.4), round(totalOccupants*0.6))
    print(temp[i] , " | " , rating , " | " , currentOccupants ,  " | " ,totalOccupants)
### High Rating + High Safe Occupancy
for i in range(150, 200):
    rating = round(random.uniform(4, 5),2)
    totalOccupants = random.randint(100, 1000)
    currentOccupants = random.randint(round(totalOccupants*0.4), round(totalOccupants*0.6))
    print(temp[i] , " | " , rating , " | " , currentOccupants ,  " | " , totalOccupants)
### Uniform Random Data
for i in range(200, 290):
    rating = round(random.uniform(1, 5),2)
    totalOccupants = random.randint(100, 1000)
    currentOccupants = random.randint(0, totalOccupants)
    print(temp[i] , " | " , rating , " | " , currentOccupants ,  " | " , totalOccupants)
### Illegal Data (Teehee)
for i in range(290, 300):
    rating = round(random.uniform(4, 5),2)
    totalOccupants = random.randint(100, 1000)
    currentOccupants = random.randint(totalOccupants, 2*totalOccupants)
    print(temp[i] , " | " , rating , " | " , currentOccupants ,  " | " , totalOccupants)

