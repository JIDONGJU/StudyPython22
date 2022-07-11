from django.db import models
from django.forms import IntegerField

# Create your models here.
class Course(models.Model):
    # 변수이름 == 컬럼이름
    name = models.CharField(max_length=255)
    cnt = models.IntegerField(null=True)