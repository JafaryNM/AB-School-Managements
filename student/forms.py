
from email.policy import default
from django import forms
from .models import Results

class ViewSingleSubjectResultForm(forms.ModelForm):
    class Meta:
        model=Results
        fields=['subject','darasa','exam']
class ViewResultsForm(forms.ModelForm):
    class Meta:
        model=Results
        fields=['darasa','exam']

class AddResultsForm(forms.ModelForm):
    class Meta:
        model=Results
        fields=['darasa','exam', 'subject']

class ResultsForm(forms.ModelForm):
    subject = forms.CharField(max_length=39)
    class Meta:
        model=Results
        fields=['mark',]
class InputResultsForm(forms.ModelForm):
    class Meta:
        model=Results
        fields=['darasa','exam', 'subject']

class InputMultipleResultsForm(forms.Form):
    """FORM FOR ADDING MULTIPLE STUDENT RESULTS USING ARRAY"""
    student=forms.IntegerField(required=False)
    mark=forms.FloatField(required=False,max_value=100,min_value=0)



