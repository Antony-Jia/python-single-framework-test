import time

def nextsequenceId(lastId):
    newId = millis = int(round(time.time() * 1000)) << 20
    if(newId <= lastId):
        return lastId + 1;
    else:
        return newId
