from django import forms
from crudtasks.models import Tasks
class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"