from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def indexView(request):
    return render(request,'index.html')


@login_required
def statementView(request):
    return render(request,'statementhuku.html')

def loginView(request):
    return render(request,'login/login.html')
