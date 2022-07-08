from django.contrib.auth.models import User
from django import forms

# 회원 가입을 위한 FORM
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # 각 필드의 clean 메소드가 호출된 후에 호출되는 메소드. 유효성 검사나 조작을 하고싶을 때 사용
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']