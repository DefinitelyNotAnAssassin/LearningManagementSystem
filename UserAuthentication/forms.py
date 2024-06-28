from UserAuthentication.models import Account
from django.forms import ModelForm, CharField, PasswordInput, ValidationError, TextInput, EmailInput, FileInput

class UserForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
    username = CharField(widget=TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Username', 'required': True}))
    email = CharField(widget=EmailInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Email', 'required': True}))
    first_name = CharField(widget=TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'id': 'name', 'name': 'name', 'type': 'text', 'placeholder': 'First Name', 'required': True}))
    last_name = CharField(widget=TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'id': 'name', 'name': 'name', 'type': 'text', 'placeholder': 'Last Name', 'required': True}))
    role = CharField(widget=TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'id': 'name', 'name': 'name', 'type': 'text', 'placeholder': 'Role', 'required': True}))
    level = CharField(widget=TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'id': 'name', 'name': 'name', 'type': 'text', 'placeholder': 'Level', 'required': True}))
    picture = CharField(widget=FileInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'id': 'name', 'name': 'name', 'type': 'file', 'placeholder': 'Picture', 'required': True}))
    password = CharField(widget=PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Password', 'required': True}))

    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'level', 'password', 'confirm_password', 'picture']
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        return cleaned_data

class LoginForm(ModelForm): 
    username = CharField(widget=TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Username', 'required': True}))
    password = CharField(widget=PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Password', 'required': True}))
    
    class Meta: 
        model = Account 
        fields = ['username', 'password']
   
    