from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


from django.db import models


class Document(models.Model):
    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document= models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    def __str__(self):
        return f'{self.user.username} Profile'