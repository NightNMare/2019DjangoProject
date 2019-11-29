from django.db import models

# Create your models here.

class Category(models.Model):
    #ID Name ItemID
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    itemid = models.IntegerField()
    def __str__(self):
        return self.name
        
class Contents(models.Model):
    #ID Title Date Contents Author Category(Category ID)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField('date published')
    contents = models.CharField(max_length=10000)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
