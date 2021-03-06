from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    token = models.AutoField(primary_key=True)  # ID
    name_zh = models.CharField(max_length=50)  # 名稱
    password = models.CharField(max_length=50)  # 密碼
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)  # 銀行

    def __str__(self):
        return self.name_zh

class Location(models.Model):
    id = models.AutoField(primary_key=True) #
    city = models.CharField(max_length=50) #縣市
    town = models.CharField(max_length=50) #鄉鎮
    district = models.CharField(max_length=50) #區

    def __str__(self):
        return self.district

class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name_zh = models.CharField(max_length=50)  # 名稱

    def __str__(self):
        return self.name_zh

class Record(models.Model):
    id = models.AutoField(primary_key=True) #
    commodity_id = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    quest_person = models.ForeignKey('User', on_delete=models.CASCADE)  # 要求者
    #own_person = models.ForeignKey('User', related_name='own_person', on_delete=models.CASCADE)  # 擁有者
    name_zh = models.CharField(max_length=50)  # 商品名稱
    type = models.ForeignKey('Type', on_delete=models.CASCADE)  # 類型
    company = models.ForeignKey('Company', on_delete=models.CASCADE) #運送公司
    date = models.CharField(max_length=50) #日期

class Company(models.Model): #輸入好供參考
    id = models.AutoField(primary_key=True) #
    name_zh = models.CharField(max_length=50)  #

    def __str__(self):
        return self.name_zh

class Type(models.Model): #輸入好供參考
    id = models.AutoField(primary_key=True) #
    name_zh = models.CharField(max_length=50)  #

    def __str__(self):
        return self.name_zh

class Commodity(models.Model):
    id = models.AutoField(primary_key=True) #
    own_person = models.ForeignKey('User', on_delete=models.CASCADE)  # 擁有者
    name_zh = models.CharField(max_length=50)  # 商品名稱
    type = models.ForeignKey('Type', on_delete=models.CASCADE)  # 類型
    describe = models.CharField(max_length=50)  # 描述
    state = models.ForeignKey('State', on_delete=models.CASCADE)  # 狀態
    location = models.ForeignKey('Location', on_delete=models.CASCADE)  # 地點

    def __str__(self):
        return self.name_zh

class State(models.Model): #輸入好供參考
    id = models.AutoField(primary_key=True) #
    name_zh = models.CharField(max_length=50)  #

    def __str__(self):
        return self.name_zh
