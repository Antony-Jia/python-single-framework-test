

from core.timeline.model.searchparamter import SearchParamter
from core.timeline.timelinequeue import TimelineQueue


# 
# 创建时间线服务 
#
class Timelinestore:
    
    #创建时间队列
    def createTimelineQueue(self, userId, type) -> TimelineQueue:
        pass

    
    #创建时间队列进行搜索
    def search(self,searchparamter:SearchParamter):
        pass


    #刷新所有数据进行存储
    def flush(self):
        pass


    #刷新管理时间线
    def close(self):
        pass


    #复原时间线
    def recover(self, queueId) -> TimelineQueue:
        pass