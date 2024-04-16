from tortoise import Model, fields


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    type = fields.CharField(max_length=255, null=True)
    description = fields.TextField(null=True)

    price = fields.FloatField(default=0.0, null=True)

    class Meta:
        table = "products"
