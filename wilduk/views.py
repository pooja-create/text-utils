from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



def delo(request):
    s = '''<h2>navigation bar</h2>
         <a href="">facebook</a>
         <a href="">google</a>
         <a href="">twitter</a>

    '''
    return HttpResponse(s)

def analyze(request):

    djtext = request.POST.get('text','default')
    removepunc=  request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc=="on":
       punctutions= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analyzed = ""
       for char in djtext:
         if char not in punctutions:
          analyzed = analyzed+char

       params={'purpose':'removed punctuations','analyzed_text': analyzed}
       djtext = analyzed

    if fullcaps == "on":
        analyzed  = ""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'new line changer', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extra line changer', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc !="on" and fullcaps!= "on"  and newlineremover!= "on" and extraspaceremover!="on"):
        return HttpResponse("Please select any operation and try again")
    return render(request, 'analyze.html', params)
