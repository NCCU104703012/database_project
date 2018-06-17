from django.shortcuts import render
from main_search.models import Commodity, User, Record, Bank, Type, Location, State
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

def add_commodity(request):
    return render(request, 'set_commodity.html')

def set_commodity(request):
    if request.method == "GET":
        own_person_get = request.GET["own_person"]
        name_zh_get = request.GET["name_zh"]
        type_get = request.GET["type"]
        describe_get = request.GET["describe"]
        location_get = request.GET["location"]
    else :
        return render(request, 'set_commodity_fail.html')

    own_person_object = User.objects.filter(name_zh = own_person_get )
    if own_person_object.count() != 1 :
        return render(request, 'set_commodity_fail.html')

    type_object = Type.objects.filter(name_zh = type_get )
    if type_object.count() != 1 :
        return render(request, 'set_commodity_fail.html')

    location_object = Location.objects.filter(district = location_get )
    if location_object.count() != 1 :
        return render(request, 'set_commodity_fail.html')

    state_object = State.objects.filter(name_zh = 'avaliable' )
    if state_object.count() != 1 :
        return render(request, 'set_commodity_fail.html')

    commodity = Commodity()
    commodity.own_person = own_person_object[0]
    commodity.name_zh = name_zh_get
    commodity.type = type_object[0]
    commodity.describe = describe_get
    commodity.location = location_object[0]
    commodity.state = state_object[0]

    return render(request, 'set_commodity_success.html')
