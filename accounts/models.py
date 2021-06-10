from django.db import models

# Create your models here.

class User_profile(models.Model):
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=200)
    college=models.CharField(max_length=200,blank=True)
    year_study=models.CharField(max_length=200,blank=True)
    total_quizzes_given=models.IntegerField(blank=True,default=0)
    average_score=models.IntegerField(blank=True,default=0)
    profile_img=models.ImageField(upload_to="photos/%y/%m/",blank=True,default='aaaaaaa.jpeg')
    
    def __str__(self):
        return str(self.user_name)