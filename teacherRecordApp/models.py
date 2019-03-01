from django.db import models
from django.utils import timezone
# Create your models here.

# Teacher name, school, subject, hours, date of work, and date of entry.
class ClassRecordModel(models.Model):
    teacherName= models.CharField(max_length=50,default='')
    school= models.CharField(max_length=100,default='')
    subject= models.CharField(max_length=40,default='')
    hours=models.IntegerField(default=0)
    workDate=models.DateField(default=timezone.now())
    entryDate=models.DateField(default=timezone.now())
        #this will list the teachers and the school they work at as well as hours logged and such
    def __str__(self):
        return(f'Instructor: {self.teacherName}')