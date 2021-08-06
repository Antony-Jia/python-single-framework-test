
from concurrent import futures
from util.messageidgenerate import nextsequenceId
from core.timeline.timelinecallback import TimelineCallBack
from core.timeline.model.timelineentry import TimelineEntry
from core.timeline.model.timelinemessage import TimelineMessage
from core.timeline.timelinequeue import TimelineQueue

class TimelineQueueImpl(TimelineQueue):
    

    def init(self):
        pass

    #获取队列ID
    def getQueueId():
        pass


    #消息存储
    async def store(self, tlm:TimelineMessage) -> TimelineEntry :
        sequenceId = nextsequenceId(0)
        await tlm.save()
        tle = TimelineEntry()
        tle.sequenceId = sequenceId
        tle.timelinemessage_id = tlm.id
        await tle.save()
        return tle

    #消息存储
    async def store(self, sequenceId, tlm:TimelineMessage) -> TimelineEntry :
        await tlm.save()
        tle = TimelineEntry()
        tle.sequenceId = sequenceId
        tle.timelinemessage_id = tlm.id
        await tle.save()
        return tle

    #消息异步存储
    async def storeAsync(self, tlm:TimelineMessage, callBack:TimelineCallBack) -> futures:
        pass


    async def storeAsync(self, sequenceId, tlm:TimelineMessage, callBack:TimelineCallBack) -> futures:
        pass