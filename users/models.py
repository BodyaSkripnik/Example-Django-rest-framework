from django.db import models
from pytz import unicode
from shortuuid.django_fields import ShortUUIDField
from projects.models import Project



USER_TYPE_CHOICES = [
    ('Entrepreneur', 'Entrepreneur'),
    ('Expert', 'Expert'),
]

DEFAULT_USER_TYPE = 'Entrepreneur'

class Role(models.Model):
    user_type = models.CharField(max_length = 100, choices = USER_TYPE_CHOICES, default = DEFAULT_USER_TYPE)
    title = models.CharField(max_length = 150, null = False, blank = False)


class Participant(models.Model):
    id = ShortUUIDField(length = 10, prefix="id_", primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length = 150, null = True, blank = False)
    photo = models.ImageField(upload_to='media/',blank=True)
    roles = models.ManyToManyField(Role, blank = True)

    
    def __str__(self):
        return unicode(self.name)

class Comment(models.Model):
    id = ShortUUIDField(length = 10, prefix="id_", primary_key=True)
    title = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    participant = models.ForeignKey(Participant,related_name='participant',on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='project',on_delete=models.CASCADE)

    
    def __str__(self):
        return unicode(self.title)