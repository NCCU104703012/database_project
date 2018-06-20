from django.shortcuts import render
from django import forms
from main_search.models import Commodity, User, Location, Type, State, Record, Company, Bank

def set_bank(request):
    bank_object = Bank.objects.filter(name_zh = '臺灣銀行' )
    if bank_object.count() == 0 :
        bank = Bank()
        bank.name_zh = '臺灣銀行'
        bank.save()

    bank_object = Bank.objects.filter(name_zh = '玉山銀行' )
    if bank_object.count() == 0 :
        bank = Bank()
        bank.name_zh = '玉山銀行'
        bank.save()

    bank_object = Bank.objects.filter(name_zh = '第一銀行' )
    if bank_object.count() == 0 :
        bank = Bank()
        bank.name_zh = '第一銀行'
        bank.save()

    bank_object = Bank.objects.filter(name_zh = '國泰世華銀行' )
    if bank_object.count() == 0 :
        bank = Bank()
        bank.name_zh = '國泰世華銀行'
        bank.save()

    bank_object = Bank.objects.filter(name_zh = '華南銀行' )
    if bank_object.count() == 0 :
        bank = Bank()
        bank.name_zh = '華南銀行'
        bank.save()

    return render(request, 'set_attribute_done.html')

def set_state(request):
    state_object = State.objects.filter(name_zh = 'avaliable' )
    if state_object.count() == 0 :
        state = State()
        state.name_zh = 'avaliable'
        state.save()

    state_object = State.objects.filter(name_zh = 'Unavaliable' )
    if state_object.count() == 0 :
        state = State()
        state.name_zh = 'Unavaliable'
        state.save()

    return render(request, 'set_attribute_done.html')

def set_company(request):
    company_object = Company.objects.filter(name_zh = '黑貓宅急便' )
    if company_object.count() == 0 :
        company = Company()
        company.name_zh = '黑貓宅急便'
        company.save()

    company_object = Company.objects.filter(name_zh = '大榮物流' )
    if company_object.count() == 0 :
        company = Company()
        company.name_zh = '大榮物流'
        company.save()

    company_object = Company.objects.filter(name_zh = '台灣宅配通' )
    if company_object.count() == 0 :
        company = Company()
        company.name_zh = '台灣宅配通'
        company.save()

    return render(request, 'set_attribute_done.html')

def set_type(request):
    type_object = Type.objects.filter(name_zh = '服飾' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '服飾'
        type.save()

    type_object = Type.objects.filter(name_zh = '化妝品' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '化妝品'
        type.save()

    type_object = Type.objects.filter(name_zh = '食物' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '食物'
        type.save()

    type_object = Type.objects.filter(name_zh = '書籍' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '書籍'
        type.save()

    type_object = Type.objects.filter(name_zh = '電子產品' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '電子產品'
        type.save()

    type_object = Type.objects.filter(name_zh = '家具' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '家具'
        type.save()

    type_object = Type.objects.filter(name_zh = '五金用品' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '五金用品'
        type.save()

    type_object = Type.objects.filter(name_zh = '票券' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '票券'
        type.save()

    type_object = Type.objects.filter(name_zh = '其他' )
    if type_object.count() == 0 :
        type = Type()
        type.name_zh = '其他'
        type.save()

    return render(request, 'set_attribute_done.html')

def set_location(request):
    location_object = Location.objects.filter(district = '三重區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '三重區'
        location.save()

    location_object = Location.objects.filter(district = '板橋區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '板橋區'
        location.save()

    location_object = Location.objects.filter(district = '中和區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '中和區'
        location.save()

    location_object = Location.objects.filter(district = '永和區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '永和區'
        location.save()

    location_object = Location.objects.filter(district = '新莊區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '新莊區'
        location.save()

    location_object = Location.objects.filter(district = '土城區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '土城區'
        location.save()

    location_object = Location.objects.filter(district = '蘆洲區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '蘆洲區'
        location.save()

    location_object = Location.objects.filter(district = '汐止區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '汐止區'
        location.save()

    location_object = Location.objects.filter(district = '樹林區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '樹林區'
        location.save()

    location_object = Location.objects.filter(district = '鶯歌區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '鶯歌區'
        location.save()

    location_object = Location.objects.filter(district = '三峽區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '三峽區'
        location.save()

    location_object = Location.objects.filter(district = '淡水區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '淡水區'
        location.save()

    location_object = Location.objects.filter(district = '新店區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '新店區'
        location.save()

    location_object = Location.objects.filter(district = '瑞芳區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '瑞芳區'
        location.save()

    location_object = Location.objects.filter(district = '五股區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '五股區'
        location.save()

    location_object = Location.objects.filter(district = '林口區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '林口區'
        location.save()

    location_object = Location.objects.filter(district = '金山區' )
    if location_object.count() == 0 :
        location = Location()
        location.city = '台北'
        location.town = '台北'
        location.district = '金山區'
        location.save()

    return render(request, 'set_attribute_done.html')
