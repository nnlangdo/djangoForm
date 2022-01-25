
from typing import final
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PersonalForm
from .models import Personal
# from .forms import DetailForm
# Create your views here.


def addform(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            data = Personal(name=name, email=email)
            data.save()
        else:
            form = PersonalForm()
    return render(request, 'addform.html', {'form':form})

def thanks(request):
    return render(request, 'thanks.html')

def about(request):
    return render(request, 'about-us.html')

def sport(request):
    return render(request, 'sport.html')

def politics(request):
    return render(request, 'politics.html')

# def calculator(request):
#     c = ""
#     try:
#         if request.method=='POST':
#             n1 = eval(request.POST.get('num1'))
#             n2 = eval(request.POST.get('num2'))
#             opr = request.POST.get('opr')

#             if opr=="+":
#                 c = n1 + n2
#             elif opr == "-":
#                 c = n1 - n2
#             elif opr == "*":
#                 c = n1 * n2
#             elif opr == "/":
#                 c = n1/n2       

#     except:
#         c="Invalid Opr........."
    
#     return render(request, 'calculator.html', {'c':c, 'n1':n1, 'n2':n2})

# def evenoddNumber(request):
#     c = ""
#     if request.method == "POST":
#         if request.POST.get('num1')== "":
#             return render(request, "evenodd.html",{'error':True})
#         n = eval(request.POST.get('num1'))
#         if n%2 == 0:
#             c = "Even Number"
#         else:
#             c = "Odd Number"
#         return render(request, 'evenodd.html',{'c':c, 'n':n} )
#     return render(request, 'evenodd.html')

# def marksheet(request):
#     if request.method == "POST":
#         s1 = eval(request.POST.get('subject1'))
#         s2 = eval(request.POST.get('subject2'))
#         s3 = eval(request.POST.get('subject3'))
#         s4 = eval(request.POST.get('subject4'))
#         s5 = eval(request.POST.get('subject5'))
#         t = s1 + s2 + s3 + s4 + s5
#         p = t*100/500
#         if p>=60:
#             d = ("First Div")
#         elif p>=45<60:
#             d = ("Second Div")
#         elif p>=35<45:
#             d = ("Third Div")
#         else:
#             d = ("Failed")
#         data = {
#             'total':t,
#             'per':p,
#             'div':d
#         }
#         return render(request, 'marksheet.html',data)
#     return render(request, 'marksheet.html')

# def detail(request):
#     if request.method == 'POST':
#         form = DetailForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')

#     else:
#         form = DetailForm()
#     return render(request, 'name.html', {'form':form})




