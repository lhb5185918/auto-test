from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # 使用 set_password 方法来哈希密码
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, verbose_name='用户名', db_index=True, unique=True)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    phone = models.CharField(max_length=11, verbose_name='手机号', unique=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_staff = models.BooleanField(default=False)  # 是否为管理员
    is_active = models.BooleanField(default=True)  # 是否激活

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    class Meta:
        db_table = 'Auto_user_info'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ['user_id']


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=30, verbose_name='项目名称')
    project_type = models.CharField(max_length=30, verbose_name='项目类型')
    project_desc = models.TextField(verbose_name='项目描述')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'Auto_project_info'
        verbose_name = '项目表'
        verbose_name_plural = verbose_name
        ordering = ['project_id']
