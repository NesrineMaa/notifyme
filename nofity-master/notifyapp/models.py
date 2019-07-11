from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.

class Category(models.Model):
    namec = models.CharField(max_length=100)
    class Meta:
        db_table = "category"


class Url(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookpublish')
    # posted_date = models.DateField(default=timezone.now)
    url = models.CharField(max_length=200)
    nameurl = models.CharField(max_length=200)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "url"



class Notif(models.Model):

    id = models.OneToOneField(Url, on_delete=models.CASCADE, related_name='bookpublish', primary_key=True)
    Nb_notif = models.IntegerField(default=True)
    Static_notif = models.IntegerField(default=True)




    class Meta:
        db_table = "Notif"






