from django.db import models

from django.contrib.auth.models import UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



class CostumUserManger(UserManager):
    pass


class User(AbstractBaseUser, PermissionsMixin):

    ROLE = (
        ('admin', 'مدیر'),
        ('user', 'کاربر'),
    )

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(max_length=15, verbose_name='نام کاربری', unique=True,
                                validators=[username_validator],
                                error_messages={
                                    "unique": "A user with that username already exists.",
                                },)
    email = models.EmailField(
       'ایمیل', unique=True, null=True, blank=True)
    role = models.CharField('نقش کاربر ', max_length=20, choices=ROLE, default="user", blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CostumUserManger()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کابران"

    def __str__(self):
        return self.username
