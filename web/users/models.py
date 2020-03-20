from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
from web.users.constant import Gender


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='user_profile', null=False)
    bio = models.TextField(null=True)
    gender = models.IntegerField(choices=Gender.FieldStr.items(), default=Gender.male, null=False)
    created_ts = models.DateTimeField(_("Created Date"), auto_now_add=True)
    updated_ts = models.DateTimeField(_("Last Updated Date"), auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "users_profile"
        verbose_name_plural = "User Profile"

