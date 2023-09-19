from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    publisher = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default= 5, 
                                         validators=[MaxValueValidator(5), MinValueValidator(1)])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    

    def __str__(self):
        return self.title