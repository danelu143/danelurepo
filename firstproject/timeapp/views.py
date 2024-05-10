from django.shortcuts import render
from django.http import HttpResponse
import datetime

def date_info(request):
    d=datetime.datetime.now()
    j=int(d.strftime("%H"))
    msg="<h1> HI FRIENDS"
    if(j<12):
        msg+=" Good Mornig Friend"
    elif(j<16):
        msg+=" Good Afternoon Friend"
    elif(j<21):
        msg+=" Good Eving Friend"
    else:
        msg+=" Good Night Friend"
    msg+="</h1>"
    msg+="<h1> Now the server time is:"+str(d)+"</h1>"

    return HttpResponse(msg)

