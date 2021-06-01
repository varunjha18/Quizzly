from django.shortcuts import render
from quizzes.models import Quiz
from quizzes.models import Question
from django.shortcuts import get_object_or_404, render


# Create your views here.
def home(request):
    all_quizzes=Quiz.objects.all()
    data={'all_quizzes':all_quizzes}
    return render(request,'home.html',data)


def start_quiz(request,quiz_id):
    quiz_start= get_object_or_404(Quiz,pk=quiz_id)
    # print('sbsfndfnnnnnnnnnnnnnnnnnnnnnnnnnnd dddddddddddddddddddddddddddddddddddd')
    data={
        'quiz_start':quiz_start,
    }
    return render(request,"quiz_start.html",data)



def question(request,quiz_id):
    questions = Question.objects.filter(quiz_id=quiz_id)
        
    result=[]
    if request.method=="POST":
        for i in range(len(questions)):
            # print(request.POST.get('question-'+str(i+1)+'-answers'))
            ans_given=(request.POST.get('question-'+str(i+1)+'-answers'))
            right_ans=questions[i].correct_answer
            
            if ans_given==None:
                result.append(-1)
            elif str(ans_given)==str(right_ans):
                result.append(1)
            else:
                result.append(0)

        print(result)
        
    data={
        'questions':questions,
        'quiz_id':quiz_id,
    }
    return render(request,"questions.html",data)