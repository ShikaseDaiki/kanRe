from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# ユーザー作成の際の設定
class UserManager(BaseUserManager):
    # 通常ユーザーの設定
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("メールアドレスは必須です")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    # スーパー(アドミン)ユーザーの設定
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=50)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email

class Pantry(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="pantry_user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class IngredientType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=40)
    pantry_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="ingredient_pantry", on_delete=models.CASCADE)
    amount = models.IntegerField()
    expirty_date = models.DateField()
    Ingredient_type = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="ingredient_ingredientType",on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name