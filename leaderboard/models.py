from django.db import models

# Create your models here.
class Score(models.Model):
    user_id=models.IntegerField()
    quiz_id=models.IntegerField()
    score=models.IntegerField(default=0)
    user_name=models.CharField(max_length=200)
    # user_name=models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.user_name)