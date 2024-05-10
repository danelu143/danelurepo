from django.shortcuts import render

def news_info(request):

    return render(request,'newsapp/news.html')
def movi_info(request):
    type='movi'
    return render(request,'newsapp/demo.html',{'type':type})
def new_info(request):
    type='new'
    return render(request,'newsapp/demo.html',{'type':type})
def poli_info(request):
    type='poli'
    return render(request,'newsapp/demo.html',{'type':type})
