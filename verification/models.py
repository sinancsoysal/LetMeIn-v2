import uuid

from django.db import models


class Verification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.CharField(max_length=255, null=True)
    uploadStatus = models.CharField(max_length=10, default="AUTHORIZED")
    completed = models.BooleanField(default=False)
