import bingmapsapi
from problemJSON import problemJSON

# From VRP-CLI interopability documents
# https://reinterpretcat.github.io/vrp/examples/interop/python.html
import subprocess
import json

cli_path = "./vrp-cli"

class Deserializer:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

class SolverClient:
    def __init__(self, cli_path):
        self.cli_path = cli_path

    def solve_pragmatic(self, problem_path, solution_path, routing_matrix_path):
        # NOTE: modify example to pass matrix, config, initial solution, etc.
        p = subprocess.run([self.cli_path, 'solve', 'pragmatic', problem_path,
            '-o', solution_path, '-m', routing_matrix_path, '--log'])
        print(p.returncode)
        if p.returncode == 0:
            with open(solution_path, 'r') as f:
                solution_str = f.read()
                return json.loads(solution_str, object_hook=Deserializer.from_dict)
        else:
            pass

def parseTestCases(filename):
    tests = []
    trucks = 0
    locationList = []
    nPickup = 0
    nDestinations = 0
    with open(filename) as f:
        line = f.readline()
        while line:
            if "trucks" in line:
                trucks = int(line[0])
            elif "Pickup Points" in line:
                line = f.readline()
                while not line.isspace():
                    locationList.append(line[:-1])
                    nPickup += 1
                    line = f.readline()
            elif "Destination Points" in line:
                line = f.readline()
                while not line.isspace():
                    locationList.append(line[:-1])
                    nDestinations += 1
                    line = f.readline()
                tests.append([trucks, locationList, nPickup, nDestinations])
                trucks = 0
                locationList = []
                nPickup = 0
                nDestinations = 0
            line = f.readline()
    return tests

def solve(tests):
    solver = SolverClient(cli_path)
    for i in range(len(tests)):
        trucks, locationList, nPickup, nDestinations = tests[i]
        problem_path = f"problem{i}.json"
        solution_path = f"solution{i}.json"
        routing_matrix_path = f"routing_matrix{i}.json"
        coordinateList = bingmapsapi.geocaching(locationList)
        with open(f"locationTest{i}.txt", "w") as f:
            f.write(str(coordinateList))
        distanceMatrix = bingmapsapi.distanceMatrix(coordinateList)
        with open(f"distanceMatrix{i}.txt", "w") as f:
            f.write(str(distanceMatrix))
        problemJSON(distanceMatrix, nPickup, nDestinations, problem_path, routing_matrix_path)
        solution = solver.solve_pragmatic(problem_path, solution_path, routing_matrix_path)
    
    
#if __name__ == "__main__":
#    tests = parseTestCases("sprint2tests.txt")
#    solve(tests)
