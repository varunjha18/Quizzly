from os import truncate
from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField

option_choices=(('A','A'),
('B','B'),
('C','C'),
('D','D'),
('E','E'),
('F','F'),
('G','G'))
# Create your models here.
class Question(models.Model):
    quiz_id=models.IntegerField(default=id)
    question_no=models.IntegerField()
    problem=models.TextField()
    option_1=models.CharField(max_length=200)
    option_2=models.CharField(max_length=200)
    option_3=models.CharField(max_length=200)
    option_4=models.CharField(max_length=200,default='None of these')
    option_5=models.CharField(max_length=200,blank=True)
    option_6=models.CharField(max_length=200,blank=True)
    option_7=models.CharField(max_length=200,blank=True)
    correct_answer=MultiSelectField(choices=option_choices)
    prob_img_1=models.ImageField(upload_to="photos/%y/%m/%d/",blank=True)
    prob_img_2=models.ImageField(upload_to="photos/%y/%m/%d/",blank=True)
    prob_img_3=models.ImageField(upload_to="photos/%y/%m/%d/",blank=True)
    points=models.IntegerField(default=10)
    date_created=models.DateTimeField(blank=True,default=datetime.now())

    def __str__(self):
        return str(self.quiz_id)



class Quiz(models.Model):
    quiz_id=models.IntegerField()
    quiz_title=models.CharField(max_length=200)
    cover_img=models.ImageField(upload_to="photos/%y/%m/%d/",blank=True)
    is_public=models.BooleanField(default=True)

    def __str__(self):
        return str(self.quiz_id)