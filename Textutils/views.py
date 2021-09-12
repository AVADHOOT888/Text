from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Textutils/home.html')

def result(request):
    text=request.POST.get('text','default')
    # print(text)
    # print(request.POST.get('upper'))
    punc=request.POST.get('removepunc','off')
    upper=request.POST.get('upper','off')
    space=request.POST.get('removespace','off')
    lower=request.POST.get('lower','off')
    
    if(upper=="on"):
        uppertext=text.upper()
        # print("upper: ",uppertext)
    else:
        uppertext=""

    if(lower=="on"):
        lowertext=text.lower()
        # print("lower: ",lowertext)
    else:
        lowertext=''

    if(punc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        puncanalyzed=""
        for i in text:
            if i not in punctuations:
                puncanalyzed+=i
        # print("punc: ",puncanalyzed)
    else:
        puncanalyzed=""
    if(space=="on"):
        spanalyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1]==" "):
                spanalyzed = spanalyzed + char
        # print("space: ",spanalyzed)
    else:
        spanalyzed =""
    
    context={"uppertext":uppertext,"lowertext":lowertext,"puncanalyzed":puncanalyzed,"spanalyzed":spanalyzed}
    return render(request, 'Textutils/result.html',context)


