from django.db import models
from shortuuid.django_fields import ShortUUIDField
from pytz import unicode

class Project(models.Model):
    id = ShortUUIDField(length = 10, prefix="id_", primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length = 150, null = True, blank = False)
    photo = models.ImageField(upload_to='media/',blank=True)

    def __str__(self):
        return unicode(self.name)
