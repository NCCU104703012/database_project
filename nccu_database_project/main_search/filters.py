from django import forms
from main_search.models import Commodity, User, Location, Type, State
import django_filters

class CourseFilter(django_filters.FilterSet):
    id = django_filters.CharFilter()
    #own_person = django_filters.CharFilter()
    location = django_filters.ModelMultipleChoiceFilter(queryset=Location.objects.all(), widget=forms.CheckboxSelectMultiple)
    type = django_filters.ModelMultipleChoiceFilter(queryset=Type.objects.all(), widget=forms.CheckboxSelectMultiple)
    state = django_filters.ModelMultipleChoiceFilter(queryset=State.objects.all(), widget=forms.CheckboxSelectMultiple)
    name_zh = django_filters.CharFilter()

    class Meta:
        model = Commodity
        fields = ['id', 'own_person', 'name_zh', 'type', 'state', 'location']
