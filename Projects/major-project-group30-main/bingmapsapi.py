import urllib.request
import urllib.parse
import json
BingMapsKey = ''

def geocaching(addressList):
    coordinateList = []
    for address in addressList:
        cleanAddress = address.translate(str.maketrans('','','.,:+')) #remove special characters (Bing API requirement)
        locationQuery = urllib.parse.quote(cleanAddress) # make address URL safe
        includeNeighborhood = 0 # Do not include neighborhood information.
        maxResults = 5 # maxinu number of locations to return
        includeValue = 'ciso2' #includes two-letter ISO country code
        url = f"http://dev.virtualearth.net/REST/v1/Locations/{locationQuery}?includeNeighborhood={includeNeighborhood}&maxResults={maxResults}&include={includeValue}&key={BingMapsKey}"
        with urllib.request.urlopen(url) as req: 
            reqjson = req.read() # default JSON
        response = json.loads(reqjson) #dictionary
        # Error Handling?
        # What to do if multiple addresses? Unknown
        coordinateList.append(response["resourceSets"][0]["resources"][0]["point"]["coordinates"])
    return coordinateList

def distanceMatrix(coordinateList):
    origins = ';'.join([str(coordinate)[1:-1] for coordinate in coordinateList]) # puts it into lat0, lon0; lat1, lon1;... latN, lonN
    origins = urllib.parse.quote(origins)
    origins = origins.replace('.', '%2E')
    distanceUnit = "mi"
    destinations = origins
    travelMode="driving"
    url = f"http://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins={origins}&destinations={destinations}&travelMode={travelMode}&key={BingMapsKey}&distanceUnit={distanceUnit}"
    with urllib.request.urlopen(url) as req: 
        reqjson = req.read() # default JSON
    response = json.loads(reqjson) #dictionary
    # travelDistance in miles, travelDuration in minutes
    return response["resourceSets"][0]["resources"][0]["results"]
