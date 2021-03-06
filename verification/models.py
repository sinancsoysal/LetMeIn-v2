from django.db import models


class Verification(models.Model):
    data = models.CharField(max_length=255)
    uploadStatus = models.CharField(max_length=10, default="AUTHORIZED")
    completed = models.BooleanField(default=False)


class ShortenedId(models.Model):
    verificationId = models.ForeignKey(Verification, on_delete=models.CASCADE)
    shortened = models.CharField(max_length=6)
    used = models.IntegerField(default=0)
