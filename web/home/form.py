from django import forms
from .models import Feedback
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
    def clean_name(self):
        name = self.cleaned_data['name']
        l = len(name)
        if l > 5 :
            raise forms.ValidationError('Invalid value')
        return name
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('com'):
            raise forms.ValidationError('Invalid value')
        return email    