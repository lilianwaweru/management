from django.db import models

# Create your models here.
class Work(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=True)
    first_name = models.CharField(max_length =30)
    other_names = models.CharField(max_length =30)
    department = models.CharField(max_length =30)
    employee_number = models.IntegerField()
    identification_number = models.IntegerField()
    nssf_number = models.IntegerField()
    nhif_number = models.IntegerField()
    date_of_birth= models.DateField()
    employee_position = models.CharField(max_length =30)
    secondary_shool = models.CharField(max_length =100)
    higher_education = models.CharField(max_length =100)
    level_of_education = models.CharField(max_length =100)
    course = models.CharField(max_length =100)
    other_certificates = models.CharField(max_length =100)
    company = models.CharField(max_length =100)
    position = models.CharField(max_length =100)
    duration = models.IntegerField()
    tasks = models.CharField(max_length =1000)
    

    objects = models.Manager()

    def save_Work(self):
        self.save()

