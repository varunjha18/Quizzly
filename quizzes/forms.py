from django import forms
from django.db import models
from django.db.models import fields
from .models import Quiz


class quizform(forms.ModelForm):
    class Meta:
        model= Quiz
        fields='__all__'