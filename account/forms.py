from django import  forms




class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget = forms.TextInput(attrs={'class' : 'form-control' } ),  max_length=100,required=True)
    password = forms.CharField(label="Password", 
    widget=forms.PasswordInput(attrs={'class' : 'form-control'}),
      max_length=100,required=True)