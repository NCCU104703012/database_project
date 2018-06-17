from django.shortcuts import render
from main_search.models import Commodity, User
from .filters import CommodityFilter

# Create your views here.
def search(request):
    Commodity_list = Commodity.objects.all()
    Commodity_filter = CommodityFilter(request.GET, queryset=Commodity_list)
    return render(request, 'Commodity_list.html', {'filter': Commodity_filter})
