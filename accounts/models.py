from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):
    clg_start = models.DateField(null=True, default=date.today)
    clg_end = models.DateField(null=True, default=date.today)
    #clg_end = models.DateField(auto_now_add=True)
    clg_type_choices = (('1','1일'),('5','5일'),('10','10일'),('20','20일'),('30','30일'),('50','50일'),('100','100일'))
    clg_type = models.TextField(max_length=10, choices=clg_type_choices, default='10')
    clg_iter_choices=(('1','1회'),('3','3회'),('5','5회'),('10','10회'),('20','20회'))
    clg_iter = models.TextField(max_length=10, choices=clg_iter_choices, default='5')
    
    noti_bool_choices = (('yes','켜기'),('no','끄기'))
    noti_bool = models.TextField(choices = noti_bool_choices, default='yes')
    noti_time_choices = (('07','07시'),('08','08시'),('09','09시'),('10','10시'),('11','11시'),('12','12시'),('13','13시'),('14','14시'),('15','15시'),('16','16시'),('17','17시'),('18','18시'),('19','19시'),('20','20시'),('21','21시'),('22','22시'),('23','23시'))
    noti_time = models.TextField(choices = noti_time_choices, default='10')
    
    user_gender_choices = (('male','남성'),('female','여성'))
    user_gender = models.TextField(null=True, blank=True, choices=user_gender_choices, default='male')
    user_height = models.IntegerField(null=True, blank=True, default=175)
    user_weight = models.IntegerField(null=True, blank=True, default=70)
    
    calorie = models.IntegerField(null=True, blank=True, default=0)
    get_point = models.IntegerField(null=True, blank=True, default=0)
    accum_point = models.IntegerField(null=True, blank=True, default=0)
    attend = models.IntegerField(null=True, blank=True, default=0)
    success_fail = models.IntegerField(null=True, blank=True, default=0)
       
# Create your models here.
