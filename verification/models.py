import uuid

from django.db import models


class Verification(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    data = models.CharField(max_length=255, null=True)
    uploadStatus = models.CharField(max_length=10, default="AUTHORIZED")
    completed = models.BooleanField(default=False)
