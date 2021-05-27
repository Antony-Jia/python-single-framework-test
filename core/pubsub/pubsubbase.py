
from abc import abstractmethod, ABCMeta

class PubSubBase(metaclass = ABCMeta):
    
    @classmethod
    @abstractmethod
    def publish(cls, topic, args):
        pass

    @classmethod
    @abstractmethod    
    def subscribe(cls, topic, function):
        pass