# accounts/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    """
    نموذج مستخدم مخصص يعتمد على AbstractUser
    يحتوي على البريد الإلكتروني ورقم الجوال كحقول إضافية
    ويستخدم related_name لتفادي تعارض مع User الافتراضي.
    """

    email = models.EmailField(
        unique=True,
        verbose_name="البريد الإلكتروني"
    )

    phone_number = models.CharField(
        max_length=15,
        verbose_name="رقم الجوال",
        blank=True
    )

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        verbose_name="المجموعات",
        blank=True,
        help_text='المجموعات التي ينتمي إليها هذا المستخدم.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        verbose_name='صلاحيات المستخدم',
        blank=True,
        help_text='صلاحيات محددة لهذا المستخدم.'
    )

    def __str__(self):
        return self.username
