from django.shortcuts import render

# Create your views here.
def register(request):
    template ='register.html'
    context={'title':'PayRep'}
    return render(request,template, context)


def login(request):
    template = 'login.html'
    context={'title':'PayRep'}
    return render(request, template, context)