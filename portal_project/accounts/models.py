from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from user_profile.models import UserProfile


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None, *args, **kwargs):
        if not email:
            raise ValueError("User must be have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        user = UserAccount.objects.get(email=email)
        user_profile = UserProfile(
            user,
            first_name="",
            last_name="",
            phone="",
            address="",
            avatar="",
        )
        user_profile.save()

        return user

    # def create_superuser(self, name, email, password, **extra_fields):
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_superuser", True)

    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError("Superuser must have is_staff=True.")
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError("Superuser must have is_superuser=True.")

    #     return self.create_user(name, email, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin, models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    can_do_anything = models.BooleanField(default=True)
    user_types = [
        ("1", "admin"),
        ("2", "teacher"),
        ("3", "student"),
    ]
    user_type = models.CharField(max_length=255, choices=user_types, default="1")
    only_read = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    school_library_manage = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
