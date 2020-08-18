from django import forms

class ClassesForm(forms.Form):
    period1 = forms.CharField(required=False, max_length=100, label="Period 1", widget=forms.TextInput(attrs={'class': 'periodField'}))
    period2 = forms.CharField(required=False, max_length=100, label="Period 2", widget=forms.TextInput(attrs={'class': 'periodField'}))
    period3 = forms.CharField(required=False, max_length=100, label="Period 3", widget=forms.TextInput(attrs={'class': 'periodField'}))
    period4 = forms.CharField(required=False, max_length=100, label="Period 4", widget=forms.TextInput(attrs={'class': 'periodField'}))