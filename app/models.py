from PIL import Image
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    rating = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'

class Racer(models.Model):
    image = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    # characteristics (for a circle)
    reaction = models.IntegerField(default=1)
    strategic_thinking = models.IntegerField(default=1)
    mental_toughness = models.IntegerField(default=1)
    g_force_withstanding = models.IntegerField(default=1)
    car_understanding = models.IntegerField(default=1)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'Racer'
        verbose_name_plural = 'Racers'

class Admin(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

class Bolide(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Bolide'
        verbose_name_plural = 'Bolides'