from django.db import models

# Create your models here.
class Feature(models.Model):

    title = models.CharField(max_length=30)
    decription = models.CharField(max_length=150)
    icons = models.CharField(max_length=30,default='icons')
    
    def __str__(self):
        return self.title

class Service(models.Model):

    name = models.CharField(max_length=30)
    decription = models.CharField(max_length=150)
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Team(models.Model):

    name = models.CharField(max_length=20)
    deg = models.CharField(max_length=20)
    img = models.ImageField(upload_to='image',null=True,blank=True)

    def __str__(self):
        return self.name

class Rating(models.Model):

    name = models.CharField(max_length=20)
    count = models.IntegerField()
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Price(models.Model):

    p_type = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.p_type

class Skill(models.Model):
    decription = models.CharField(max_length=150)
    s_width = models.IntegerField()
    e_width = models.IntegerField()
    a_width = models.IntegerField()
    img = models.ImageField(upload_to='image',null=True,blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=30)
    deg = models.CharField(max_length=20)
    des = models.CharField(max_length=30)
    img = models.ImageField(upload_to='image',null=True,blank=True)


class Contect(models.Model):

    add = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10,default='')



class Feedback(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    msg = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=30)
    des = models.TextField()
    img = models.ImageField(upload_to='image',null=True,blank=True)

    def __str__(self):
        return self.title

class Works(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='image',null=True,blank=True)
    w_type = models.CharField(max_length=10,default='all')    