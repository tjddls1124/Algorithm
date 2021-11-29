import requests
import json

x_auth_token = '5ac42796d16f98497505d51548490383'
base_url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'


header = {'X-Auth-Token':x_auth_token, 'Content-Type': 'application/json'}
data = {'problem':1}

res = requests.post(base_url+"/start",data=json.dumps(data), headers=header)

auth_key = res.json()['auth_key']

def getInfo(st):
    #locations, trucks, score
    h = {'Authorization':auth_key, 'Content-Type': 'application/json' }
    return requests.get(base_url+"/"+st,headers= h).json()

def simulate(command):
    h = {'Authorization':auth_key, 'Content-Type': 'application/json' }
    data = {"commands": command}
    return requests.put(base_url+"/simulate",data=json.dumps(data), headers=h).json()
    ## [{"truck_id": 0, "command": [0, 0]}]

NO = 0
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4
LOAD = 5
UNLOAD = 6

## Most-To-Least
def goAtoB(a,b):
    command = []
    a_row = a//5
    a_col = a%5
    b_row = b//5
    b_col = b%5
    move = 0
    if a_row < b_row:
        move=RIGHT
    else:
        move=LEFT    
    for i in range(abs(b_row - a_row)):
        command.append(move)
    
    if a_col < b_col:
        move=UP
    else:
        move=DOWN 
    for i in range(abs(b_col - a_col)):
        command.append(move)
        
    return command

def getMost():
    max_v = 0
    max_l = 0
    for v in getInfo("locations")['locations']:
        if max_v < v['located_bikes_count'] :
            max_v = v['located_bikes_count']
            max_l = v['id']
    
    return max_l,max_v
def getLeast():
    max_v = 1000
    max_l = 0
    for v in getInfo("locations")['locations']:
        if max_v > v['located_bikes_count'] :
            max_v = v['located_bikes_count']
            max_l = v['id']
    
    return max_l,max_v

def setLoc():
    arr = []
    for v in getInfo("locations")['locations']:
        arr.append(v['located_bikes_count'])
    return arr

def setTruckLoc():
    arr = []
    for v in getInfo("trucks")['trucks']:
        arr.append(v['location_id'])
    return arr

def moveToBase():
    cmd = []
    for i in range(5):
        cmd.append(makeCommand(i, goAtoB(truck_arr[i], 12)))
    return cmd

def mostToLeast(tid):
    mo_index, mo_val = getMost()
    le_index, le_val = getLeast()
    command = []
    if mo_val > 4:
        command.extend(goAtoB(truck_arr[tid], mo_index))
        command.append(LOAD)
        command.append(LOAD)
        command.extend(goAtoB(mo_index, le_index))
        command.append(UNLOAD)
        command.append(UNLOAD)
        print(command)
    return command

def makeCommand(tid,command):
    return {"truck_id":tid, "command":command}



loc_arr = setLoc()
print(loc_arr)
truck_arr = setTruckLoc()
print(truck_arr)

simulate(moveToBase())
for _ in range(19):
    simulate([{"truck_id": 0, "command": [0, 0]}])

loc_arr = setLoc()
print(loc_arr)
truck_arr = setTruckLoc()
print(truck_arr)

simulate([makeCommand(0, mostToLeast(0))])

loc_arr = setLoc()
print(loc_arr)
truck_arr = setTruckLoc()
print(truck_arr)
print(getInfo("trucks"))
