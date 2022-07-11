from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models(=테이블) here.
# class name == Table name
class Curriculum(models.Model):
    # 변수이름 == 컬럼이름
    name = models.CharField(max_length=255)