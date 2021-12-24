from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyFarmerManager(BaseUserManager):
    def create_user(self, first_name , last_name, username, email, phone, password=None):
        if not first_name:
            raise ValueError("User must have First Name")
        if not last_name:
            raise ValueError("User must have Last Name")
        if not username:
            raise ValueError("User must have UserName")
        if not email:
            raise ValueError("User must have Email")
        if not phone:
            raise ValueError("User must have Phone Number")

        user = self.model(
            email = self.normalize_email(email),
            username= username,
            first_name= first_name,
            last_name= last_name,
            phone= phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Buyer(AbstractBaseUser):
    first_name = models.CharField(verbose_name='first name', max_length=200, null=True)
    last_name = models.CharField(verbose_name='last name', max_length=200, null=True)
    username = models.CharField( max_length=200, unique=True)
    email = models.EmailField(verbose_name='email', null=True, unique=True)
    phone = models.CharField(verbose_name='phone number',max_length=200, null=True)
    profile_pic = models.ImageField(verbose_name='profile_pic', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone']

    object = MyFarmerManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
