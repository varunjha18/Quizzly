from django.shortcuts import render

# Create your views here.

def leaderboard(request,quiz_id):
    return render(request,'leaderboard.html')