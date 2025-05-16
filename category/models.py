from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def getall(cls):
        return cls.objects.filter(is_deleted=False)

    @classmethod
    def Add(cls, name, description=""):
        return cls.objects.create(name=name, description=description)

    @classmethod
    def update(cls, id, name, description=""):
        cls.objects.filter(id=id).update(name=name, description=description)

    @classmethod
    def softdelete(cls, id):
        cls.objects.filter(id=id).update(is_deleted=True)

    @classmethod
    def harddelete(cls, id):
        cls.objects.filter(id=id).delete()
