from django.db import models

# Create your models here.
SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)
  
# declaring a Student Model
  
class Student(models.Model):
      name = models.CharField(max_length=50)
      roll_no = models.IntegerField(unique=True)
      semester = models.CharField(max_length =20,choices = SEMESTER_CHOICES,default = '1')
      
