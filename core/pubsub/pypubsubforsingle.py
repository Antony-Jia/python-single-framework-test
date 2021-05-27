from pubsub import pub
from pubsubbase import PubSubBase

class PyPubSubforSingle (PubSubBase):

    def publish(cls, topic, args):
        pub.sendMessage(topic, arg1=args)

    def subscribe(cls, topic, function):
        pub.subscribe(function, topic)
    


# pubsub = PyPubSubforSingle()
# print('test')

# def listener1(arg1):
#     print('Function listener1 received:')
#     print('  arg1 =', arg1)

# pubsub.subscribe('rootTopic', listener1)

# print('Publish something via pubsub')
# anObj = dict(a=456, b='abc')
# pubsub.publish('rootTopic', 123)