from tortoise.models import Model
from tortoise import fields

class TimelineMessage(Model):

    id = fields.IntField(pk=True)

    source = fields.TextField()
    destination = fields.TextField()
    context = fields.TextField()
    type = fields.TextField()
    externalId = fields.TextField()
    time = fields.DateField() 



    class Meta:
        table = "timeline_message"

    def __str__(self):
        return self.name

        