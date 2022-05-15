from os import name
from tokenize import Name
from xml.etree.ElementTree import Comment
from django.db import models
from django.utils import timezone

# Create your models here.
class IbAccountPage1(models.Model):
    star_status=[
        ('checked','checked'),
        ('','')
    ]
    exclusive=[
        ('star','star'),
        ('','')
    ]
    name =models.CharField(max_length=550)
    IB_number =models.IntegerField()
    photo =models.ImageField(upload_to='photos')
    client_NO =models.IntegerField()
    typye = models.CharField(max_length=50,choices=exclusive,null=True,blank=True)
    star1 =models.CharField(max_length=50,choices=star_status,null=True,blank=True)
    star2 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star3 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star4 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star5 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star6 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    telegram_link=models.CharField(max_length=500,null=True,blank=True)
    instagram_link=models.CharField(max_length=500,null=True,blank=True)
    facebook_link=models.CharField(max_length=500,null=True,blank=True)
    IB_link= models.CharField(max_length=500,null=True,blank=True)
    
    def __str__(self):
        return self.name

class IbAccountPage2(models.Model):
    star_status=[
        ('checked','checked'),
        ('','')
    ]
    exclusive=[
        ('star','star'),
        ('','')
    ]
    name =models.CharField(max_length=550)
    IB_number =models.IntegerField()
    photo =models.ImageField(upload_to='photos')
    client_NO =models.IntegerField()
    typye = models.CharField(max_length=50,choices=exclusive,null=True,blank=True)
    star1 =models.CharField(max_length=50,choices=star_status,null=True,blank=True)
    star2 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star3 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star4 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star5 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star6 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    telegram_link=models.CharField(max_length=500,null=True,blank=True)
    instagram_link=models.CharField(max_length=500,null=True,blank=True)
    facebook_link=models.CharField(max_length=500,null=True,blank=True)
    IB_link= models.CharField(max_length=500,null=True,blank=True)
    
    def __str__(self):
        return self.name

class IbAccountPage3(models.Model):
    star_status=[
        ('checked','checked'),
        ('','')
    ]
    exclusive=[
        ('star','star'),
        ('','')
    ]
    name =models.CharField(max_length=550)
    IB_number =models.IntegerField()
    photo =models.ImageField(upload_to='photos')
    client_NO =models.IntegerField()
    typye = models.CharField(max_length=50,choices=exclusive,null=True,blank=True)
    star1 =models.CharField(max_length=50,choices=star_status,null=True,blank=True)
    star2 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star3 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star4 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star5 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star6 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    telegram_link=models.CharField(max_length=500,null=True,blank=True)
    instagram_link=models.CharField(max_length=500,null=True,blank=True)
    facebook_link=models.CharField(max_length=500,null=True,blank=True)
    IB_link= models.CharField(max_length=500,null=True,blank=True)
    
    def __str__(self):
        return self.name

class IbAccountPage4(models.Model):
    star_status=[
        ('checked','checked'),
        ('','')
    ]
    exclusive=[
        ('star','star'),
        ('','')
    ]
    name =models.CharField(max_length=550)
    IB_number =models.IntegerField()
    photo =models.ImageField(upload_to='photos')
    client_NO =models.IntegerField()
    typye = models.CharField(max_length=50,choices=exclusive,null=True,blank=True)
    star1 =models.CharField(max_length=50,choices=star_status,null=True,blank=True)
    star2 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star3 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star4 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star5 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star6 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    telegram_link=models.CharField(max_length=500,null=True,blank=True)
    instagram_link=models.CharField(max_length=500,null=True,blank=True)
    facebook_link=models.CharField(max_length=500,null=True,blank=True)
    IB_link= models.CharField(max_length=500,null=True,blank=True)
    
    def __str__(self):
        return self.name

class IbAccountPage5(models.Model):
    star_status=[
        ('checked','checked'),
        ('','')
    ]
    exclusive=[
        ('star','star'),
        ('','')
    ]
    name =models.CharField(max_length=550)
    IB_number =models.IntegerField()
    photo =models.ImageField(upload_to='photos')
    client_NO =models.IntegerField()
    typye = models.CharField(max_length=50,choices=exclusive,null=True,blank=True)
    star1 =models.CharField(max_length=50,choices=star_status,null=True,blank=True)
    star2 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star3 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star4 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star5 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    star6 = models.CharField(max_length=50, choices=star_status, null=True, blank=True)
    telegram_link=models.CharField(max_length=500,null=True,blank=True)
    instagram_link=models.CharField(max_length=500,null=True,blank=True)
    facebook_link=models.CharField(max_length=500,null=True,blank=True)
    IB_link= models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    NameOfIb = models.CharField(max_length=250,null=True,blank=True)
    link= models.CharField(max_length=2555,null=True,blank=True)
    Titel = models.CharField(max_length=250,null=True,blank=True)
    Description = models.TextField(max_length=50,null=True,blank=True)
    photo =models.ImageField(upload_to='photos')
    post_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.NameOfIb
    class Meta:
        ordering=('-post_date',)

class About(models.Model):
    Titel = models.CharField(max_length=250,null=True,blank=True)
    Description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Titel

class Opinion(models.Model):
    Name = models.CharField(max_length=250)
    TheComment = models.TextField(max_length=500)
    # active = models.BooleanField(default=False)

    def __str__(self):
        return self.Name
class Offer(models.Model):
    act=[
        ('active','active'),
        (' ',' ')
    ]
    Titel = models.CharField(max_length=250,null=True,blank=True)
    first = models.CharField(max_length=50,choices=act,null=True,blank=True)
    photo =models.ImageField(upload_to='photos',null=True,blank=True)

    def __str__(self):
        return self.Titel


class Education(models.Model):
    Name = models.CharField(max_length=250,null=True,blank=True)
    link= models.CharField(max_length=2555,null=True,blank=True)
    Titel = models.CharField(max_length=250,null=True,blank=True)
    Description = models.TextField(max_length=50,null=True,blank=True)
    photo =models.ImageField(upload_to='photos')
    post_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Name
    # class Meta:
    #     ordering=('-post_date',)