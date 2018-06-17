from django.shortcuts import render
from main_search.models import Commodity, User
from .filters import CourseFilter

# Create your views here.
def search(request):
    user_list = Commodity.objects.all()
    user_filter = CourseFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})
