from django import forms

class FormInciarSesion(forms.Form):
	username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','id':'s_input_email','placeholder':'Correo Electronico'}))
	password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control','id':'s_input_password','placeholder':'Contrasena'}))