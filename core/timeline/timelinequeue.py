
#
#时间线队列
#
from core.timeline.timelinecallback import TimelineCallBack
from core.timeline.model.timelinemessage import TimelineMessage
from core.timeline.model.timelineentry import TimelineEntry

from concurrent.futures import ThreadPoolExecutor, Future

class TimelineQueue:


    def init():
        pass
    
    #获取队列ID
    def getQueueId():
        pass

    
    #消息存储
    def store(self, tlm:TimelineMessage) -> TimelineEntry :
        pass

    #消息存储
    def store(self, sequenceId, tlm:TimelineMessage) -> TimelineEntry :
        pass

    #消息异步存储
    def storeAsync(self, tlm:TimelineMessage, callBack:TimelineCallBack) -> Future:
        pass


    #消息异步存储
    def storeAsync(self, sequenceId, tlm:TimelineMessage, callBack:TimelineCallBack) -> Future:
        pass