from tortoise import Model, fields


class Supplier(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    location = fields.CharField(max_length=255, null=True)
    category = fields.CharField(max_length=255, null=True)

    description = fields.TextField(null=True)

    products = fields.OneToOneField("models.Product", related_name="suppliers")

    class Meta:
        table = "suppliers"
