from django.db import models
#from django.contrib.postgres.fields import ArrayField

class Character(models.Model):
       
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50, blank = True, null = True)
    #occupation = ArrayField(models.CharField(max_length=50, blank=True, null= True), size=8)
    img = models.CharField( max_length=250, blank = True, null = True)
    status = models.CharField( max_length=50, blank = True, null = True)
    nickname = models.CharField( max_length=50, blank = True, null = True)
    #appearance = ArrayField(models.IntegerField(), size=6)
    #better_call_saul_appearance = ArrayField(models.IntegerField(), size=6)
    portrayed = models.CharField( max_length=50, blank = True, null = True)
    category = models.CharField( max_length=100, blank = True, null = True)

    def __str__(self):
        return self.name

    objects = models.Manager()

class Episode(models.Model):

    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=50, blank = True, null = True)
    season = models.IntegerField()
    episode = models.IntegerField()
    air_date = models.CharField(max_length=50, blank = True, null = True)
    #characters = ArrayField(models.CharField(max_length=50, blank=True, null= True), size=20)
    series = models.CharField(max_length=100, blank = True, null = True)

    def __str__(self):
        return self.title
    
    objects = models.Manager()

class Quote(models.Model):

    id = models.IntegerField(unique=True, primary_key=True)
    quote = models.CharField(max_length=100, blank = True, null = True)
    author = models.CharField(max_length=50, blank = True, null = True)
    series = models.CharField(max_length=100, blank = True, null = True)

    def __str__(self):
        return self.quote
    
    objects = models.Manager()
