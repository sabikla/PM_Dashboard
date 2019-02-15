from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gitlab_token = models.CharField(max_length=100, null=True, blank=True)
    gitlab_url = models.URLField(default="gitlab.com")
