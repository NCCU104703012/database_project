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
