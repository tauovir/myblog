from django.db import models
import datetime
# Create your models here.

# Contactus Form table
class Contactus(models.Model):
    name = models.CharField(max_length=100,null=False) # max_length required
    email = models.EmailField(max_length=120,null=False) # max_length required
    message = models.TextField(max_length=800,null=False) # max_length required
    created_at = models.DateField(default=datetime.date.today) 
    class Meta:
        db_table = 'contactus'
        
    def __str__(self):
        return  self.name
