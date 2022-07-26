import urllib.request
import urllib.parse
import json

def problemJSON(distanceMatrix, nPickup, nDestinations, problem_path, routing_matrix_path):
    #formats a valid pragmatic dataset for vrp-cli
    #vrp-cli solve pragmatic problem.json -o solution.json -m routing_matrix.json --log
    jobs = []
    vehicles = []
    travelTimes = []
    distances=[]
    for i in range(nDestinations):
        #List of jobs
        jobs.append({"id":"d"+str(i),"services":[{"places":[{"location":{"index":i+nPickup},"duration":0}]}]})
    for i in range(nPickup):
        #List of vehicles
        vehicles.append({"typeId":"vehicle"+str(i),"vehicleIds":["vehicle"+str(i)], "profile":{"matrix":"DistanceMatrix"}, "costs": {"fixed":0,"time":0, "distance":1},
                         "shifts": [{"start":{"earliest":"2019-07-04T09:00:00Z","location":{"index":i}}}], "capacity":[50]})
    for entry in distanceMatrix:
        #distance matrix
        #There's an integer programming constraint. round distances to nearest meter, times to nearest second
        travelTimes.append(round(entry["travelDuration"]*60))
        distances.append(round(entry["travelDistance"]*1000))
    routing_matrix = {"profile":"DistanceMatrix","travelTimes":travelTimes,"distances":distances}
    with open(routing_matrix_path,'w') as f:
        f.write(json.dumps(routing_matrix))
    profiles = [{"name":"DistanceMatrix"}]
    plan={'jobs':jobs}
    fleet={'vehicles':vehicles, 'profiles':profiles}
    problem = {"plan":plan, "fleet":fleet}
    with open(problem_path, 'w') as f:
        f.write(json.dumps(problem))
            
