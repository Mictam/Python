from django import forms

class NoteForm(forms.Form):
    date_id = forms.DateField(widget=forms.DateInput(attrs={'class' : 'form-control','placeholder' : 'Data: YYYY-MM-DD', 'style': 'margin-top:10px; margin-bottom:10px', 'aria-describedby': 'add-btn' }))

    content = forms.CharField(max_length=500,
            widget=forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'Treść...' }))

class EditForm(forms.Form):
    content = forms.CharField(max_length=500,
            widget=forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'Treść...' }))