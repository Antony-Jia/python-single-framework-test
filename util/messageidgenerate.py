import time
import datetime

def nextsequenceId(lastId):
    newId = millis = int(round(time.time() * 1000)) << 20
    if(newId <= lastId):
        return lastId + 1;
    else:
        return newId

def getSequenceIdDaysAgo(days):
    timestamp = (datetime.datetime.now() - datetime.timedelta(days=30)).timestamp()
    newId = millis = int(round(timestamp * 1000)) << 20
    return newId

# print(nextsequenceId(0))
# print(time.time())
# print(datetime.datetime.now().timestamp())
# print((datetime.datetime.now() - datetime.timedelta(days=30)).timestamp())
print(getSequenceIdDaysAgo(30))