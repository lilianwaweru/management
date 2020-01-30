from django.db import models

# Create your models here.
class Master(models.Model):
    first_name = models.CharField(max_length =30)
    other_names = models.CharField(max_length =30)
    identification_number = models.IntegerField()
    nssf_number = models.IntegerField()
    nhif_number = models.IntegerField()
    date_of_birth= models.DateField()
    employee_number = models.IntegerField()
    employee_position = models.CharField(max_length =30) 
    
    objects = models.Manager()

    def save_Master(self):
        self.save()


class Education(models.Model):
    secondary_shool = models.CharField(max_length =100)
    higher_education = models.CharField(max_length =100)
    level_of_education = models.CharField(max_length =100)
    course = models.CharField(max_length =100)
    other_certificates = models.CharField(max_length =100)

    # objects = models.Education()

    def save_Education(self):
        self.save()


class Work(models.Model):
    company = models.CharField(max_length =100)
    position = models.CharField(max_length =100)
    duration = models.IntegerField()
    tasks = models.CharField(max_length =1000)



