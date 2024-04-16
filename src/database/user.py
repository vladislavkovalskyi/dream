from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    uid = fields.IntField(null=False)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)

    business = fields.ManyToManyField("models.Business", related_name="users")
    supplier = fields.ManyToManyField("models.Supplier", related_name="users")
    
    class Meta:
        table = "users"
