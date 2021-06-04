from django.shortcuts import redirect, render
from quizzes.models import Quiz
from quizzes.models import Question
from django.shortcuts import get_object_or_404, render
from .forms import quizform


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
        score=0
        for i in range(len(questions)):
            # print(request.POST.get('question-'+str(i+1)+'-answers'))
            ans_given=(request.POST.get('question-'+str(i+1)+'-answers'))
            right_ans=questions[i].correct_answer
            
            if ans_given==None:
                result.append([-1,questions[i].problem,ans_given,right_ans])
            elif str(ans_given)==str(right_ans):
                result.append([1,questions[i].problem,ans_given,right_ans])
                score+=questions[i].points
            else:
                result.append([0,questions[i].problem,ans_given,right_ans])
        
        # print(result)
        res_data={
            'result':result,
            "score":score,
        }
        return render(request,"results.html",res_data)
        


    data={
        'questions':questions,
        'quiz_id':quiz_id,
    }
    return render(request,"questions.html",data)



def create_quiz(request):
    new_quiz_id=max(Quiz.objects.values_list('id',flat=True))+1
    if request.method=="POST":
        # form=quizform(data=request.POST,files=request.FILES)
        # print(form)
        # if form.is_valid():
        #     form.save()
        #     obj=form.instance
        #     print(obj)
        #     print('wwwwwwwwwwoooooooooooorrrrrrrrrrrrrrkkkkkkkkkkkkkkkkk')
        #     return render(request,"create_questions.html",{"obj":obj})
        # print('rbbbbbbbbbbbb')
        
        
        quiz_title=request.POST.get('quiz_title')
        cover_img=request.FILES.get('cover_img')
        no_of_ques=request.POST.get('no_of_ques')
        print(cover_img)
        # print(Quiz.objects.values_list('id',flat=True))
        quiz=Quiz(quiz_id=new_quiz_id,quiz_title=quiz_title,cover_img=cover_img)

        quiz.save()
        data={'no_of_ques' : range(int(no_of_ques)) }
        return render(request,'create_questions.html',data)

    return render(request,'create_quiz_start.html')



# def create_questions(request):
#     return render(request,'create_questions.html')