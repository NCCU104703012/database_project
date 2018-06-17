from django.shortcuts import render
from main_search.models import Commodity, User, Record, Bank
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

def add_user(request):
    return render(request, 'set_user.html')

def set_user(request):
    if request.method == "GET":
        name_zh_get = request.GET["name_zh"]
        password_get = request.GET["password"]
        bank_get = request.GET["bank"]
    else :
        return render(request, 'set_user_fail.html')

    name_zh_object = User.objects.filter(name_zh = name_zh_get )
    if name_zh_object.count() > 0 :
        return render(request, 'set_user_fail.html')

    bank_object = Bank.objects.filter(name_zh = bank_get )
    if bank_object.count() != 1 :
        return render(request, 'set_user_fail.html')

    user = User()
    user.name_zh = name_zh_get
    user.password = password_get
    user.bank = bank_object[0]
    user.save()

    return render(request, 'set_user_success.html')
