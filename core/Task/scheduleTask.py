import schedule
import time
import threading
import datetime
import queue
import logging


class ScheduleTask:
    
    #schedule job add lock
    lock = threading.Lock()
    #start event
    stop_run_continuously:threading.Event = None
    #schedule job thread excute queue
    jobqueue = queue.Queue(2)

    #logging setting
    logging.basicConfig()
    schedule_logger = logging.getLogger('schedule')
    schedule_logger.setLevel(level=logging.DEBUG)
    
    #singlton lock
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        with ScheduleTask._instance_lock:
            if not hasattr(ScheduleTask, "_instance"):
                ScheduleTask._instance = ScheduleTask(*args, **kwargs)
        return ScheduleTask._instance

    

    def schedulejobAddSecond(self, function, every = 1, tag = 'default'):
        self.lock.acquire()
        try:
            schedule.every(every).seconds.do(self.jobqueue.put, function).tag(tag)
        finally:
            self.lock.release()
        

    def schedulejobAddMinute(self, function, every = 1, tag = 'default'):
        self.lock.acquire()
        try:
            schedule.every(every).minutes.do(self.jobqueue.put, function).tag(tag)
        finally:
            self.lock.release()
        
    def schedulejobAddHour(self, function, every = 1, tag = 'default'):
        self.lock.acquire()
        try:
            schedule.every(every).hour.do(self.jobqueue.put, function).tag(tag)
        finally:
            self.lock.release()
        
    def schedulejobAddDay(self, function, every = 1, tag = 'default'):
        self.lock.acquire()
        try:
            schedule.every(every).day.do(self.jobqueue.put, function).tag(tag)
        finally:
            self.lock.release()
        
    def schedulejobAddMinute(self, function, every = 1, tag = 'default', at = ':0'):
        self.lock.acquire()
        try:
            schedule.every(every).minutes.do(self.jobqueue.put, function).tag(tag).at(at)
        finally:
            self.lock.release()
        
    def schedulejobAddHour(self, function, every = 1, tag = 'default', at = ':0'):
        self.lock.acquire()
        try:
            schedule.every(every).hour.do(self.jobqueue.put, function).tag(tag).at(at)
        finally:
            self.lock.release()
        
    def schedulejobAddDay(self, function, every = 1, tag = 'default', at = ':0'):
        self.lock.acquire()
        try:
            schedule.every(every).day.do(self.jobqueue.put, function).tag(tag).at(at)
        finally:
            self.lock.release()
        
    def worker_main(self):
        while 1:
            job_func = self.jobqueue.get()
            job_func()
            self.jobqueue.task_done()

    def queueStart(self):
        worker_thread = threading.Thread(target=self.worker_main)
        worker_thread.start()


    def run_continuously(self, interval=1):
        """Continuously run, while executing pending jobs at each
        elapsed time interval.
        @return cease_continuous_run: threading. Event which can
        be set to cease continuous run. Please note that it is
        *intended behavior that run_continuously() does not run
        missed jobs*. For example, if you've registered a job that
        should run every minute and you set a continuous run
        interval of one hour then your job won't be run 60 times
        at each interval but only once.
        """
        cease_continuous_run = threading.Event()

        class ScheduleThread(threading.Thread):
            @classmethod
            def run(cls):
                while not cease_continuous_run.is_set():
                    try:
                        self.lock.acquire()
                        schedule.run_pending()
                        time.sleep(interval)
                    finally:
                        self.lock.release()
                    
        continuous_thread = ScheduleThread()
        continuous_thread.start()
        return cease_continuous_run

    def start(self):
        self.queueStart()
        self.stop_run_continuously = self.run_continuously()

    def stop(self):
        self.stop_run_continuously.set()

    def get_jobs(self, findstr='default'):
        return schedule.get_jobs(findstr)

    def getAlljobs(self):
        return schedule.get_jobs()    

# def job():
#     print("1")
#     print(datetime.datetime.now())
# def job2():
#     print("2")
#     print(datetime.datetime.now())
# def job3():
#     print("3")
#     print(datetime.datetime.now())    

# st = SecheduleTask()
# st.schedulejobAddSecond(job)
# st.schedulejobAddSecond(job2)
# st.start()
# st.schedulejobAddSecond(job3)
# print(st.getAlljobs())
# print(st.get_jobs())