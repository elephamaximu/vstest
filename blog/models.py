from django.db import models
import datetime
import json
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
#class1개가 테이블1개 
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                    related_name='blog_post_set')
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def latlng_validation(value):
        check = re.match(r'(\d+\.?\d*),(\d+\.?\d*)', value)
        if not check:
            raise ValidationError("유효하지 않은 위도, 경도입니다.")

    latlng = models.CharField(max_length=100, blank=True,
                validators=[latlng_validation],
                help_text="위도와 경도를 입력하세요")

    def validation_even(value):
        if value % 2 != 0:
            raise ValidationError(str(value) + "가 짝수 이어야 합니다.")

    even_field = models.IntegerField(validators=[validation_even])
    str_field = models.CharField(max_length=50)
    str_field2 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title + " ___id는" + str(self.id)

    class Meta:
        ordering=['title', '-id']
     #   ordering=['id'] # id로 ascending 

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name

class FieldTest(models.Model):
    fAutoField = models.AutoField(primary_key=True)
    fBigIntegerField = models.BigIntegerField(default=1)
    fBooleanField = models.BooleanField(default=True)
    fCharField = models.CharField(default='엔코아', max_length=30)
    fDateField = models.DateField(auto_now=False, default=datetime.date.today)
    fDateTimeField = models.DateTimeField(auto_now=False, auto_now_add=False)
    fDecimalField = models.DecimalField(default=1.7321, decimal_places=4, max_digits=10)
    fEmailField = models.EmailField(default="email@example.com")
    fFloatField = models.FloatField(default=1.7321)
    fIntegerField = models.IntegerField(default=10)
    fGenericIPAddressField = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, default=None)
    fNullBooleanField = models.NullBooleanField(default=True)
    fPositiveIntegerField = models.PositiveIntegerField(default=100)
    fPositiveSmallIntegerField = models.PositiveSmallIntegerField(default=50)
    fSlugField = models.SlugField(max_length=30, default='slug')
    fSmallIntegerField = models.SmallIntegerField(default=-50)
    fTextField = models.TextField(default="text text text text text text text")
    fURLField = models.URLField(max_length=200, default='http://localhost')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)