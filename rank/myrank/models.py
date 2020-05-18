from django.db import models


# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20,unique=True)


class TopScore(models.Model):
    uid = models.OneToOneField(to="UserInfo", to_field='id', on_delete=models.CASCADE)
    personal_high_score = models.PositiveIntegerField(default=0)
