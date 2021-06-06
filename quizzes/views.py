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
        # data={'no_of_ques' : range(int(no_of_ques)) }
        return redirect('create_questions',new_quiz_id,int(no_of_ques))

    return render(request,'create_quiz_start.html',{'new_quiz_id':new_quiz_id})



def create_questions(request,quiz_id,no_of_ques):
    data={'no_of_ques' : range(1,int(no_of_ques)+1) ,'quiz_id':quiz_id,'number':int(no_of_ques)}
    if request.method=='POST':
        
        for j in range(no_of_ques):
            problem=request.POST.get('problem-'+str(j+1))
            print(problem)
            if problem is not None and problem is not "":
                question_no=j+1
                option_1=request.POST.get('question-'+str(j+1)+'-option-1')
                option_2=request.POST.get('question-'+str(j+1)+'-option-2')
                option_3=request.POST.get('question-'+str(j+1)+'-option-3')
                option_4=request.POST.get('question-'+str(j+1)+'-option-4')
                option_5=request.POST.get('question-'+str(j+1)+'-option-5')
                correct_ans=request.POST.get('question-'+str(j+1)+'-correct')
                print('gjwvfjkbkjbijkjkbwfewev')
            # print(problem,question_no,option_1,option_2,option_3,option_4,option_5,correct_ans)

                question=Question(quiz_id=quiz_id,problem=problem,question_no=question_no,option_1=option_1,option_2=option_2,option_3=option_3,option_4=option_4,option_5=option_5,correct_answer=correct_ans)

                question.save()

        return redirect('home')



    return render(request,'create_questions.html',data)