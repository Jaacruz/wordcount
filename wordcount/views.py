from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')
#    return render(request,'home.html',{'hithere':'Este es mi perfil.'})

def searchpage(request):
    fulltext=request.GET['fulltext']
    wordlist= fulltext.split()
    return render(request,'search.html',{'fulltext':fulltext,'search':len(wordlist)})

def aboutpage(request):
    return render(request,'about.html')
