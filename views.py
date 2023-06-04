#video 6
from django.http import HttpResponse
from django.shortcuts import render

#Main Function
def index(request):
    data={
        't1':'new page',
        't2':"submit"
    }
    return render(request,"index.html",data)

#For Puncuation
def punc(request):
   djtext=(request.POST.get('textarea','default'))
   punc=(request.POST.get('checkbox1','off'))
   cap=(request.POST.get('cap1','off'))          # here we are using post method to bring data from index .html
   space=(request.POST.get('space1','off'))
   charcount=(request.POST.get('charcount1','off'))
   data={} #blank dictionary

#puncuation method
   if punc=="on":
    print(punc)
    a=djtext
    b=""
    puncuations = '''!@#$%^&*(){}[]_-+=:;'"<>?/|\/<>'''
    for i in a:
        if i not in puncuations:
            b+=i
        data={
            't1':b}
        djtext=b

#For Capitalize
   if cap=="on":
    a=djtext
    b=a.upper()
    print(b)
    data={
            't1':b}
    djtext=b 
    
#For Spaceremover
   if space=="on":
     a=djtext
     b=""
     for i in a:
        if i==" ":
            continue
        else:
            b+=i
        data={
            't1':b}
        djtext=b
        
#CharCount Function
   if charcount=="on":
    a=djtext
    count=0
    b=""
    b=djtext
    for i in a:
        count+=1
    print(count)
    c=count
    #dictionary is created which consist of t1 and t2

    data={
        't1':b,
        't2':c
    }
    djtext=b

   #if user doesnt select any of the option
   if (charcount != "on" and space != "on" and cap != "on" and punc != "on"):
        b="PLEASE CLICK ON ONE OF THE BUTTON TO PERFORM OPERATION"
        #dictionary is created which consist of t1
        data={
        't1':b,
    }
   #with this statement we jump to data.html page and transfer data 
   return (render(request,"data.html",data))








