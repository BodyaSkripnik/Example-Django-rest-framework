import django_filters
from .models import Comment
import django_filters



class CommentsFilter(django_filters.FilterSet):
    participant = django_filters.CharFilter(field_name="participant__id")#для фильтрации(поиска по вложеностям)
    project = django_filters.CharFilter(field_name="project__id")#для фильтрации(поиска по вложеностям)
    class Meta:
        model = Comment
        fields = {
            'id': ['exact'],
            'title' : ['contains'],
            'created_date' : ['lt', 'gt'],#lt поиск до и после 
            'participant' : ['exact'],
            'project' : ['exact'],
        }