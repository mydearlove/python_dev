from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, BaseModel):
    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    addr = models.CharField(max_length=100, verbose_name='收件人地址')
    zip_code = models.IntegerField(null=True, verbose_name='邮政编码')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')
    user = models.ForeignKey(User, verbose_name='所属账户',on_delete=models.CASCADE)
    class Meta:
        db_table = 'df_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name

