from django.db import models
#
# # Create your models here.
from django.contrib.auth.base_user import BaseUserManager


# ----------회원 가입 Custom User Model------------
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,email,password,gender=1,**extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email =self.normalize_email(email)
        user = self.model(email=email,gender=gender,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",True)
        return self._create_user(email,password,**extra_fields)


    def create_superuser(self,email,password,**extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')

        return self.create_user(email,password,**extra_fields)



GENDER_CHOICE = (
    (0, "Female"),
    (1, "Man"),
    (2, "Etc")
)


class User(AbstractUser, PermissionsMixin):

    email = models.EmailField(verbose_name="email",max_length=300,unique=True)
    username = models.CharField(max_length=200)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE)
    date_joined = models.DateTimeField(("date joined"),default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"

    # username_field값과 패스원드는 기본적으로 요구

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



