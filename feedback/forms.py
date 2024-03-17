from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['food_rating', 'recommendation', 'name', 'mobile_number']
