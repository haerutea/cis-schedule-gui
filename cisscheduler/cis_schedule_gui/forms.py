from django import forms

class ClassesForm(forms.Form):
    block1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'blockField'}))
    block2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'blockField'}))
    block3 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'blockField'}))
    block4 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'blockField'}))