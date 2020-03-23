from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'index.html'
    context={'title':'PayRep'}
    return render(request,template, context)


def contact(request):
    template = 'contact.html'
    context={'title':'PayRep'}
    return render(request,template, context)


def about(request):
    template ='about.html'
    context={'title':'PayRep'}
    return render(request,template, context)



def services(request):
    template = 'services.html'
    context={'title':'PayRep'}
    return render(request,template, context)

