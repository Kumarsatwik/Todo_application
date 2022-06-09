from django.forms import ModelForm
from testapp.models import *

class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields=['title','description']