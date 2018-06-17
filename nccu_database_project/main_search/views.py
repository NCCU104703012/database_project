from django.shortcuts import render
from main_search.models import Commodity, User, Record
from .filters import CommodityFilter, RecordFilter

# Create your views here.
def search_Commodity(request):
    Commodity_list = Commodity.objects.all()
    Commodity_filter = CommodityFilter(request.GET, queryset=Commodity_list)
    return render(request, 'Commodity_list.html', {'filter': Commodity_filter})

def search_Record(request):
    Record_list = Record.objects.all()
    Record_filter = RecordFilter(request.GET, queryset=Record_list)
    return render(request, 'Record_list.html', {'filter': Record_filter})
