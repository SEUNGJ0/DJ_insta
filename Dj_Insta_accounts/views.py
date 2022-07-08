from django.shortcuts import render
from .forms import RegisterForm

# 회원 가입 FORM을 위한 VIEW
def register(request):
    # 회원 가입 정보가 서버로 전달 됐을 경우
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        # user_form이 유효하다면.
        if user_form.is_valid():
            # 폼 객체에 지정된 모델을 확인하고, 객체 생성 | commit=False --> 메모리 상에 객체만 생성
            new_user = user_form.save(commit=False)
            # set_password : 비밀번호를 지정
            new_user.set_password(user_form.cleaned_data['password'])
            # 실제로 DB에 비밀번호를 저장
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form':user_form})


