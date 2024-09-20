from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={
        'class': 'form-control custom-textinput',
        'placeholder': 'Enter page title...'
    }))
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={
        'class': 'form-control custom-textarea' ,
        'placeholder': 'Enter the Content (in Markdown)...'
    }))
