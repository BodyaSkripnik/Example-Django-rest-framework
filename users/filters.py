import django_filters
from .models import Comment
import django_filters



class CommentsFilter(django_filters.FilterSet):
    participant = django_filters.CharFilter(field_name="participant__id")
    project = django_filters.CharFilter(field_name="project__id")
    class Meta:
        model = Comment
        fields = {
            'id': ['exact'],
            'title' : ['contains'],
            'created_date' : ['lt', 'gt'],
            'participant' : ['exact'],
            'project' : ['exact'],
        }