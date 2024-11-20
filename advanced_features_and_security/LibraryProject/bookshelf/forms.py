from django import forms

class ExampleForm(forms.Form):
    field_name = forms.CharField(max_length=100, label='Example Field', required=True)
