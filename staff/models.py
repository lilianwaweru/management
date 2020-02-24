from django.db import models

# Create your models here.
class Master(models.Model):
    first_name = models.CharField(max_length =30)
    other_names = models.CharField(max_length =30)
    department = models.CharField(max_length =30)
    employee_number = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return str(self.employee_number)


    def save_Master(self):
        self.save()

    # def update_Master(self,employee_number):
    #     self.employee_number = employee_number
    #     self.save()

   


class Work(models.Model):
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
    image = models.ImageField(upload_to = 'images/',blank=True)
    employee = models.ForeignKey(Master,on_delete=models.CASCADE,null=True)

    objects = models.Manager()

    def save_Work(self):
        self.save()

