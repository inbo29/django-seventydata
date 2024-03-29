from django.shortcuts import render
from django.views.generic.base import TemplateView



def profile(request):
    return render(request, "registration/profile.html")


from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        #회원가입 데이터 입력완료
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        #회원 가입 내용을 입력하는 상황
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':user_form})