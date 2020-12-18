from django import forms
from AppTwo.models import user_info

class NewUserForm(forms.ModelForm):
    class Meta():
        model = user_info
        fields = '__all__'
