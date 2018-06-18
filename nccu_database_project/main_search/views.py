from django.shortcuts import render
from main_search.models import Commodity, User, Record, Bank, Type, Location, State, Company
from .filters import CommodityFilter, RecordFilter

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
        password_get = request.GET["password"]
        name_zh_get = request.GET["name_zh"]
        type_get = request.GET["type"]
        describe_get = request.GET["describe"]
        location_get = request.GET["location"]
    else :
        return render(request, 'set_commodity_fail.html')

    own_person_object = User.objects.filter(name_zh = own_person_get )
    if own_person_object.count() != 1 :
        return render(request, 'set_commodity_fail.html')

    if own_person_object[0].password != password_get :
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
    commodity.save()

    return render(request, 'set_commodity_success.html')

def buy_commodity(request):
    return render(request, 'buy_commodity.html')

def set_record(request):
    if request.method == "GET":
        commodity_id_get = request.GET["commodity_id"]
        quest_person_get = request.GET["quest_person"]
        password_get = request.GET["password"]
        company_get = request.GET["company"]
        date_get = request.GET["date"]
    else :
        return render(request, 'set_record_fail.html')

    try:
        commodity_id_object = Commodity.objects.filter(id = int(commodity_id_get) )
    except Exception as e:
        return render(request, 'set_record_fail.html')

    if commodity_id_object.count() != 1 :
        return render(request, 'set_record_fail.html')

    quest_person_object = User.objects.filter(name_zh = quest_person_get )
    if quest_person_object.count() != 1 :
        return render(request, 'set_record_fail.html')

    if quest_person_object[0].password != password_get :
        return render(request, 'set_record_fail.html')

    company_object = Company.objects.filter(name_zh = company_get )
    if company_object.count() != 1 :
        return render(request, 'set_record_fail.html')

    record = Record()
    record.commodity_id = commodity_id_object[0]
    record.quest_person = quest_person_object[0]
    record.name_zh = commodity_id_object[0].name_zh
    record.type = commodity_id_object[0].type
    record.company = company_object[0]
    record.date = date_get
    record.save()

    state_object = State.objects.filter(name_zh = 'Unavaliable' )
    commodity_id_object.update(state = state_object[0] )

    return render(request, 'set_record_success.html')
