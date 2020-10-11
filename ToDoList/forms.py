from  django import forms
from  .models import ToDoList

class AdListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'