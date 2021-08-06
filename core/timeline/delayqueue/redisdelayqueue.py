

from core.timeline.model.timelinemessage import TimelineMessage
from core.redisutil.redisutil import getRedisConn
import json

class RedisDelayQueue(object):
    
    def __init__(self, name):
        self.name = name
        self.zsetname = self.name + '_zset'
        self.hashname = self.name + '_hash'
        
    def insert(self, sequenceId, tlm:TimelineMessage):
        r = getRedisConn()
        r.zadd( self.zsetname, sequenceId, self.name + '_' + str(sequenceId) )
        r.hmset( self.hashname, self.name + '_' + str(sequenceId), json.dumps(tlm.__dict__) )

    def get(self, sequenceId) -> TimelineMessage:
        r = getRedisConn()
        return r.hget(self.name + '_' + str(sequenceId))

    def getAfterTimeMessage(self, sequenceId):
        r = getRedisConn()
        SequenceIds = r.zrangebyscore(self.zsetname, max=sequenceId)
        return r.hmget(self.hashname, SequenceIds)

    def getAfterTimeMessage(self, beginSequenceId, endSequenceId):
        r = getRedisConn()
        SequenceIds = r.zrangebyscore(self.zsetname, min=beginSequenceId, max=endSequenceId)
        return r.hmget(self.hashname, SequenceIds)