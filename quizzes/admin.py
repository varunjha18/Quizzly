from django.contrib import admin
from quizzes.models import Question, Quiz
from django.utils.html import format_html

# Register your models here.
class quesAdmin(admin.ModelAdmin):
    
    list_display=('quiz_id','question_no','problem',)
    # list_display_links=('car_title',)
    # list_editable= ('is_featured',)
    # search_fields=("first_name","last_name",'id')
    # list_filter=("first_name","last_name",'designation')




admin.site.register(Question,quesAdmin)
admin.site.register(Quiz)