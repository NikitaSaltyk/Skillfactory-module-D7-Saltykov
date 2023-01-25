from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    dateCreation = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}))

    category = ModelChoiceFilter(
        field_name='postCategory__name',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='Любая категория')

    class Meta:
        model = Post
        fields = {
            'author': ['exact'],
            'title': ['icontains'],
        }