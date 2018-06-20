from django import forms

class UploadFileForm(forms.Form):
    field = forms.FileField(label='Wybierz piosenkę',widget=forms.FileInput(attrs={'style':'width:100%'}))