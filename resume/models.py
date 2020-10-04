from __future__ import unicode_literals
from django.db import models

class staticVars():
    form_number = 0

class Person(models.Model):
    

    first_name = models.CharField(max_length=255,default = "rahul")
    last_name = models.CharField(max_length=255, default = "prabhakar")
    email = models.EmailField(blank=True, default = "raj@gmail.com" )
    mobile = models.CharField(max_length=15,blank=True,default= "7997056565")
    address = models.CharField(max_length=255,blank=True,default = "fulkaha")
    '''age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)'''

    def full_name(self):
        return " ".join([self.first_name, self.last_name])


class ProfileInterest(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    interest = models.CharField(max_length=20)

class WorkExperience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=255)
    position =  models.CharField(max_length=255)
    start_from =  models.CharField(max_length=255)
    end_on =  models.CharField(max_length=255)
    Discription =  models.CharField(max_length=255)


class Education(models.Model):
    DEGREE_CHOICES = (
        ('Phd', 'Doctors'),
        ('Mtech/MA/MSc/MCom/MBA', 'Masters'),
        ('BE/Btech/BA/BSc/BCom', 'Bachelors'),
        ('12th', 'High School')
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    institute = models.CharField(max_length=100, default= "nitw")
    stream = models.CharField(max_length=100, blank=True,default="ece")
    passing_year = models.CharField(max_length=100, blank=True, default ="2020")
    result = models.CharField(max_length=20, default = "9")



class ProjectOrJob(models.Model):
    WORK_CHOICES = (
        ('J', 'Job'),
        ('P', 'Project')

    )

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    work = models.CharField(max_length=1, choices=WORK_CHOICES, default = 'J')
    title = models.CharField(max_length=100,default="software developer")
    start_date = models.CharField(max_length=100,default="2016")
    end_date = models.CharField(max_length=100,default="2020")
    description = models.TextField(default="intern")


class ProfessionalSkills(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_detail = models.TextField()


class Academics(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    academic_detail = models.TextField()


class AreaOfInterest(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    area_of_interest_detail = models.TextField()
