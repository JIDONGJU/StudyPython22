from django.db import models

# Create your models here.
class Curriculum(models.Model):
    # 변수이름 == 컬럼이름
    name = models.CharField(max_length=255)