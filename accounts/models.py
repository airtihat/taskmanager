# accounts/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings


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


class GroupInvite(models.Model):
    group_name = models.CharField(max_length=100)
    email = models.EmailField()
    # تعديل هنا بإضافة related_name لتفادي التعارض
    invited_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='sent_invites')
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    # تعديل هنا أيضاً بإضافة related_name لتفادي التعارض
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='group_invite')

    def __str__(self):
        return f"{self.email} -> {self.group_name}"

    def get_invite_link(self):
        return f"{settings.SITE_URL}/accounts/register/?group={self.group_name}&email={self.email}"

