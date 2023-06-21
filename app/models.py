from django.db import models

# Create your models here.


class Country(models.Model):
    cname=models.CharField(max_length=20,primary_key=True)
    cpopulation=models.IntegerField()

    def __str__(self) -> str:
        return self.cname
    
class Capital(models.Model):
    cname=models.ForeignKey(Country,on_delete=models.CASCADE)
    capital_name=models.CharField(max_length=20)
    capital_population=models.IntegerField()

    def __str__(self) -> str:
        return self.capital_name
    
