from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def county(request):

    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1



    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddict':worddict})


def done(request):
    return render(request,'done.html',{})




