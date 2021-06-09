from django.shortcuts import render
from .models import Score

# Create your views here.

def leaderboard(request,quiz_id):
    this_quiz_leaderboard=Score.objects.filter(quiz_id=quiz_id).order_by('-score')
    # print(this_quiz_leaderboard.count())
    score_count=this_quiz_leaderboard.count()
    data={'scores':zip(this_quiz_leaderboard,range(1,score_count+1))}
    return render(request,'leaderboard.html',data)