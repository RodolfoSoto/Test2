from django import forms
from exam.models import *


class ZombieForm(forms.ModelForm):
    class Meta:
        model = Zombie


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
