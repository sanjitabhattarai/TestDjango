from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index (request):
    return render(request,'Index.html')

def mysecondpage (request):
    return render(request,'second.html')


def mythirdpage(request):
    var= "hello"
    greetings="How are you?"
    fruits=['book','copy','marker']
    num1,num2=5,7
    ans = num1 > num2
    my_dict={
        "var":var,
        "msg":greetings,
        "myfruits":fruits,
        "num1": num1,
        "num2": num2,
        "ans":ans

    }
    return render(request,'third.html',context=my_dict)



def myimagepage(request):
    return render(request,'imagepage.html')

def myformpage(request):
    return render(request,'myform.html')