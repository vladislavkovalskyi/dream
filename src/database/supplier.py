from tortoise import Model, fields


class Business(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    location = fields.CharField(max_length=255, null=True)
    budget = fields.FloatField(default=0.0, null=True)
    description = fields.TextField(null=True)
    category = fields.CharField(max_length=255, null=True)
