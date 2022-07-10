import django_filters
from .models import Comment
import django_filters



class CommentsFilter(django_filters.FilterSet):
    participant = django_filters.CharFilter(field_name="participant__id")
    project = django_filters.CharFilter(field_name="project__id")
    class Meta:
        model = Comment
        fields = ['id', 'title', 'created_date','participant','project']
