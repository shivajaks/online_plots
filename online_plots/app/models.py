from django.db import models
class Plotmodel(models.Model):
    plotno=models.IntegerField(primary_key=True)
    roadno=models.IntegerField()
    surveyno=models.IntegerField()
    cost_p_sqyard=models.IntegerField()
    total_sqyard=models.IntegerField()
    other_exp=models.IntegerField()
    facing=models.CharField(max_length=7)
    status=models.CharField(max_length=10)
    total_cost=models.IntegerField()
    image=models.ImageField(upload_to='product_images/')

class Appmodel(models.Model):
    appno = models.IntegerField(primary_key=True)
    floorno = models.IntegerField()
    surveyno = models.IntegerField()
    cost_p_sqyard = models.IntegerField()
    total_sqyard = models.IntegerField()
    other_exp = models.IntegerField()
    facing = models.CharField(max_length=7)
    status = models.CharField(max_length=10)
    total_cost = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')

class Employeemodel(models.Model):
    E_name=models.CharField(max_length=30)
    E_id=models.IntegerField(primary_key=True)
    E_email=models.EmailField()
    E_location=models.CharField(max_length=20)
    E_doj=models.DateField()
    E_remark=models.CharField(max_length=10)
