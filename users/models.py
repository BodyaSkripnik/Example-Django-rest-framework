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
    RATING_CHOICES = (
        (5, "5"),
        (4.5, "4,5"),
        (4, "4"),
        (3.5, "3,5"),
        (3, "3"),
        (2.5, "2,5"),
        (2, "2"),
        (1.5, "1,5"),
        (1, "1"),
    )

    id = ShortUUIDField(length = 10, prefix="id_", primary_key=True)
    title = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    participant = models.ForeignKey(Participant,related_name='participant',on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='project',on_delete=models.CASCADE)
    project_management_level = models.FloatField(verbose_name = 'Рівень проджект менеджменту',choices = RATING_CHOICES)
    quality_of_performance = models.FloatField(verbose_name = 'Якість виконання робіт/послуг/поставок',choices = RATING_CHOICES)
    timeliness_of_performance = models.FloatField(verbose_name = 'Своєчасність виконання робіт/послуг/поставок',choices = RATING_CHOICES)
    culture_and_speed_of_communication = models.FloatField(verbose_name = 'Культура та швидкість комунікації',choices = RATING_CHOICES)
    speed_and_quality_of_defect_elimination = models.FloatField(verbose_name = 'Швидкість та якість усунення дефектів',choices = RATING_CHOICES)
    
    def __str__(self):
        return unicode(self.title)

    # def get_full_address(self):
    #     return "%s, %s" % (self.Quality_of_performance_of_works_services_supplies, self.Timeliness_of_performance_of_works_services_deliveries)

    def get_rating(self):
        return (
            (self.quality_of_performance + \
                self.timeliness_of_performance + \
                self.project_management_level + \
                self.culture_and_speed_of_communication +\
                self.speed_and_quality_of_defect_elimination ) / 5)
