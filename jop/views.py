from django.shortcuts import render
from . models import Jop

# Create your views here.

def jop_list(reguest):
    jop_list = Jop.objects.all()
    context = {'jops' :jop_list }
    return render(reguest,'jop/jop_list.html',context)

def jop_detail(reguest , id):
    jop_detail = Jop.objects.get(id=id)
    context = {'jop' : jop_detail}
    return render(reguest , 'jop/jop_det.html' , context)
