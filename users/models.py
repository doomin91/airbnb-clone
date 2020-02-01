from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ Custom User Morel """


# DB가 아닌 FORM 을 수정하는 것이기 때문에, MIGRATION 이 필요없다

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENTER_OTEHR = "otehr"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENTER_OTEHR, "Other"),
    )

    LANGUAGE_ENGISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "Usd"),
        (CURRENCY_KRW, "Krw"),
    )

    
# char Field 는 한 줄 텍스트/글자수 제한/대부분의 경우 char 사용/choices를 통해 커스터마이징 가능
# Text Field 는 여러 줄/글자 수 제한없음

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

