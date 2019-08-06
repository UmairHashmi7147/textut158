#i have created this file
from django.http import HttpResponse
from django.shortcuts import render
"""
def index(request):
    return HttpResponse('''<h1> <a href="https://www.youtube.com/watch?v=P80gQhWbQc4&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=63" >Click for youtube page</a> </h1>''')
def about(request):
    return HttpResponse("Hello bhai")"""






def index(request):
    #params ={'name':'umair','place':'Gujrat'}
    #return render(request,'index.html',params)
     return render(request,'index.html')
  #  return HttpResponse('''<h1>  <a href="http://127.0.0.1:8000 "  >Home</a> </h1>''' '''<h1>  <a href="http://127.0.0.1:8000/spaceremover "  >Space Remover</a> </h1>''')
   # return HttpResponse('''<h1>  <a href="http://127.0.0.1:8000/spaceremover "  >Space Remover</a> </h1>''')
   #def removepunc(request):
def analyze(request):
    djtext=request.POST.get('text','default')
    rem=request.POST.get('removepunc','off')
    cap=request.POST.get('capital','off')
    newlin=request.POST.get('lineremover','off')
    params=""
    print(djtext)
    print(rem)
    #analyzed=djtext
    afterpunc=""
    afterpunc1=""
    aftercap=""
    aftercap1=""
    afternewline=""
    afternewline1=""
    afterspace=""
    afterspace1=""
    punctuations='''!()-[];:'"\,<>/?@#$%^&*_~.'''
    if rem=="on":
      afterpunc1="Text After Removing Punctuations is"
     # li="\n"
      for char in djtext:
       if char not in punctuations:
        afterpunc = afterpunc + char
    params = {'afterpunc1': afterpunc1, 'afterpunc': afterpunc, 'aftercap1': aftercap1, 'aftercap': aftercap,
              'afternewline1': afternewline1, 'afternewline': afternewline, 'afterspace': afterspace}


    if cap=="on":
     aftercap1="Text After Capitalization is"
     if afterpunc!="":
            for char in afterpunc:
             aftercap = aftercap + char.upper()
     else:
        for char in djtext:
         aftercap=aftercap+char.upper()
    params = {'afterpunc1': afterpunc1, 'afterpunc': afterpunc, 'aftercap1': aftercap1, 'aftercap': aftercap,
              'afternewline1': afternewline1, 'afternewline': afternewline, 'afterspace': afterspace}
    #return render(request,'analyzetext.html',params)
    #return HttpResponse("Remove punc")

    if newlin=="on":
     lin="\n"
     afternewline1="Text After Line Removing is"
     if afterpunc!="":
      for char in afterpunc:
        if char not in lin:
            afternewline=afternewline+char
        else:
            afternewline=afternewline+" "
     else:
      lin="\n"
      for char in djtext:
       if char not in lin:
         afternewline = afternewline + char
       else:
          afternewline = afternewline + " "
     params = {'afterpunc1': afterpunc1, 'afterpunc': afterpunc, 'aftercap1': aftercap1, 'aftercap': aftercap,
               'afternewline1':afternewline1,'afternewline': afternewline, 'afterspace': afterspace}
    return render(request, 'analyzetext.html', params)

def ex1(request):
        sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
                 '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
                 '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
                 '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
                 ]
        return HttpResponse((sites))



""" def capitalizefirst(request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremover(request):
    return HttpResponse("Space Remover")

def charcounter(request):
    return HttpResponse("Character Counter")"""