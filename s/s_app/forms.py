from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from s_app.models import CustomUser

class Form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
