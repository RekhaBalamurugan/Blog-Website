""" from django.forms import ModelForm
from .models import ModelName


class FormName(ModelForm):
    class Meta:
        model = ModelName
        fields = '__all__' """


from django.forms import ModelForm
from .models import ModelName

class NewUser(ModelForm):
    class meta:
        model=ModelName
        fields = '__all__'
