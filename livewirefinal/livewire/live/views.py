from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    print(request)
    return render(request,'home.html')
def intern(request):
      return render(request,'internship.html')
def webin(request):
      return render(request,'webinar.html')
def contacts(request):
      return render(request,'contact.html')
def recomm(request):
      return render(request,'recom.html')
def demo(c,b):
    op=Livedata.objects.filter(type=b).values()
    o1={}
    a=[]
    for i in op:
        o1['key1']=i['keytopic1'].split('*')
        o1['key2']=i['keytopic2'].split('*')
        o1['key3']=i['projectexp'].split('*')
        o1['jobroles']=i['jobroles'].split('*')
        o1['suitable']=i['suitable'].split('*')
    for i in o1['key3']:
        a.append(i.split('+'))
    o1['key3']=a
    print(o1)
    '''o1['key1']=op['keytopic1'].split('*')'''
    return render(c,'index.html',{'value1':op,'value2':o1})

def java(request):
      return demo(request,'java')
def adjava(request):
      return demo(request,'adjava')
def c(request):
      return demo(request,'c')
def ac(request): #c++
      return demo(request,'ac')
def python(request):
      return demo(request,'python')
def mern(request):
      return demo(request,'mern')
def django(request):
      return demo(request,'django')
def app(request):#kotlin
      return demo(request,'app')
def cs(request):#c Sharp
      return demo(request,'cs')
def plc(request):
      return demo(request,'plc')
def epsa(request):#electrical power system Analysis
      return demo(request,'epsa')
def matlab(request):
      return demo(request,'matlab')
def microcont(request):#microcontroller
      return demo(request,'microcont')
def neteng(request):#network engineering
      return demo(request,'neteng')
def amicrocont(request):#advanced microcontroller
      return demo(request,'amicrocont')
def netsec(request):#network security
      return demo(request,'netsec')
def ethical(request):#ethical hacking
      return demo(request,'ethical')
def ds(request):#data science
      return demo(request,'ds')
def dsde(request):#data science and data engineering
      return demo(request,'dsde')
def dsr(request):#data science using r
      return demo(request,'dsr')
def ml(request):#machine learning
      return demo(request,'ml')
def mlp(request):#machine learning using python
      return demo(request,'mlp')
def mlr(request):#machine learning using r
      return demo(request,'mlr')
def bc(request):#block chain
      return demo(request,'bc')
def ai(request):#artifical intelligence
      return demo(request,'ai')
def rpa(request):#RPA
      return demo(request,'rpa')
def robo(request):#robotics
      return demo(request,'robo')
def IOT(request):
      return demo(request,'iot')
def nlp(request):
      return demo(request,'nlp')
def tdprinting(request):#3 d printing
      return demo(request,'tdprinting')
