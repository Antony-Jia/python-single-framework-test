from util.log import Log
from core.Task.scheduleTask import ScheduleTask
from util.messageidgenerate import getSequenceIdDaysAgo
from core.redisutil.redisutil import getRedisConn


class TimeTaskForCleanDelayQueue:

    def __init__(self):
        self.namelist = []
        self.log = Log().getInstance('TimeTaskForCleanDelayQueue')

    def addName(self, name):
        self.namelist.append(name)

    #获取30天前sequenceId，在30天前的sequenceId都进行删除
    def clearOneMonthData(self, name):
        r = getRedisConn()
        oldSequenceId = getSequenceIdDaysAgo(30)
        SequenceIds = r.zrangebyscore(self.zsetname, max=oldSequenceId)
        r.zremrangebyscore(self.zsetname, max=oldSequenceId)
        return r.hdel(self.hashname, SequenceIds)


    def clearNameListData(self): 
        self.log.info("clearNameListData excute")
        for item in self.namelist:
            self.clearOneMonthData(item)       

    def setTaskJob(self):
        st = ScheduleTask()
        st.schedulejobAddDay(self.clearNameListData)
        