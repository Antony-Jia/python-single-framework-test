

#
#时间线对象，每个对象包含了信息和唯一ID
#
from core.timeline.model.timelinemessage import TimelineMessage
from tortoise.models import Model
from tortoise import fields

class TimelineEntry(Model):

    id = fields.IntField(pk=True)
    sequenceId = fields.TextField()

    timelinemessage: fields.OneToOneRelation[TimelineMessage] = fields.OneToOneField("models.TimelineMessage", on_delete=fields.CASCADE, related_name="timelineentry")
    
    class Meta:
        table = "timeline_entry"

    