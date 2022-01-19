from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fullname']
        em = request.POST['email']
        m = request.POST['mobile']
        s = request.POST['subject']
        msg = request.POST['message']
        try:
            Contact.objects.create(fullname=f, email=em, mobile=m, subject=s, message=msg,msgdate=date.today(),isread="no")
            error = "no"
        except:
            error = "yes"
    d={'error':error}
    return render(request, 'contact.html',d)

def signin(request):
    error=""
    if request.method=='POST':
        u=request.POST['eid']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signin.html',d)

def signup(request):
    error=""
    if request.method=='POST':
        f=request.POST['firstname']
        l=request.POST['lastname']
        r=request.POST['rollno']
        c=request.POST['contact']
        e=request.POST['emailid']
        p=request.POST['password']
        ba=request.POST['batch']
        b=request.POST['branch']
        sec=request.POST['section']
        try:
            u=User.objects.create_user(username=e,password=p,first_name=f,last_name=l)
            Person.objects.create(user=u,rollno=r,contact=c,batch=ba,branch=b,section=sec)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def teacher_login(request):
    error=""
    if request.method=='POST':
        u=request.POST['un']
        p=request.POST['pw']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'teacher_login.html',d)

def signout(request):
    logout(request)
    return redirect('index')

def teacher_home(request):
    if not request.user.is_staff:
        return redirect('teacher_login')
    pn=Notes.objects.filter(status="Pending",receiverType="Teacher",sendTo=str(request.user.username)).count()
    an=Notes.objects.filter(status="Accepted",receiverType="Teacher",sendTo=str(request.user.username)).count()
    rn=Notes.objects.filter(status="Rejected",receiverType="Teacher",sendTo=str(request.user.username)).count()
    sn=Notes.objects.filter(receiverType="Teacher",sendTo=str(request.user.username)).count()
    d={'pn':pn,'an':an,'rn':rn,'sn':sn}
    return render(request,'teacher_home.html',d)

def t_uploadnotes(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    user_obj=User.objects.get(id=request.user.id)
    person_obj=Person.objects.get(user=user_obj)
    error=""
    if request.method=='POST':
        u=person_obj
        batch=request.POST['batch']
        branch=request.POST['branch']
        section=request.POST['section']
        s=request.POST['subject']
        f=request.FILES['filedoc']
        ft=request.POST['filetype']
        des=request.POST['description']
        to=str(batch)+"-"+str(branch)+"-"+str(section)
        try:
            Notes.objects.create(user=u,uploadDate=date.today(),subject=s,notesFile=f,fileType=ft,description=des,status="",receiverType="Student",sendTo=to)
            error="no"
        except:
            error="yes"
    d={'person_obj':person_obj,'user_obj':user_obj,'error':error}
    return render(request,'t_uploadnotes.html')

def t_viewusers(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    persons_obj=[]
    for p in Person.objects.all():
        if p.user.is_staff==False:
            persons_obj.append(p)
    d={'persons_obj':persons_obj}
    return render(request,'t_viewusers.html',d)

def t_deleteusers(request,pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('t_viewusers')
    
def t_assignstatus(request,pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    notes=Notes.objects.get(id=pid)
    error=""
    if request.method=='POST':
        s=request.POST['status']
        try:
            notes.status=s
            notes.save()
            error="no"
            return redirect('t_allnotes')
        except:
            error="yes"
    d={'notes':notes,'error':error}
    return render(request,'t_assignstatus.html',d)

def t_pendingnotes(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    notes=Notes.objects.filter(status="Pending",receiverType="Teacher",sendTo=str(request.user.username))
    d={'notes':notes}
    return render(request,'t_pendingnotes.html',d)

def t_acceptednotes(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    notes=Notes.objects.filter(status="Accepted",receiverType="Teacher",sendTo=str(request.user.username))
    d={'notes':notes}
    return render(request,'t_acceptednotes.html',d)

def t_rejectednotes(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    notes=Notes.objects.filter(status="Rejected",receiverType="Teacher",sendTo=str(request.user.username))
    d={'notes':notes}
    return render(request,'t_rejectednotes.html',d)

def t_allnotes(request):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    notes=Notes.objects.filter(receiverType="Teacher",sendTo=str(request.user.username))
    d={'notes':notes}
    return render(request,'t_allnotes.html',d)

def t_deletenotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('teacher_login')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('t_allnotes')

def student_home(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    user_obj=User.objects.get(id=request.user.id)
    person_obj=Person.objects.get(user=user_obj)
    d={'person_obj':person_obj,'user_obj':user_obj}
    return render(request,'student_home.html',d)

def s_changepassword(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    error=""
    if request.method=="POST":
        o=request.POST['opwd']
        n1=request.POST['npwd1']
        n2=request.POST['npwd2']
        u=User.objects.get(username__exact=request.user.username)
        if n2==n1 and u.check_password(o):
            u.set_password(n1)
            u.save()
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request,'s_changepassword.html',d)

def s_editprofile(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    user_obj=User.objects.get(id=request.user.id)
    person_obj=Person.objects.get(user=user_obj)
    error=False
    if request.method=='POST':
        f=request.POST['firstname']
        l=request.POST['lastname']
        c=request.POST['contact']
        user_obj.first_name=f
        user_obj.last_name=l
        person_obj.contact=c
        user_obj.save()
        person_obj.save()
        error=True
    d={'person_obj':person_obj,'user_obj':user_obj,'error':error}
    return render(request,'s_editprofile.html',d)

def s_uploadnotes(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    user_obj=User.objects.get(id=request.user.id)
    person_obj=Person.objects.get(user=user_obj)
    all_usernames=[]
    persons=Person.objects.all()
    for p in persons:
        if(p.user.is_staff==True):
            all_usernames.append(p.user.username)
    error=""
    if request.method=='POST':
        u=person_obj
        s=request.POST['subject']
        se=request.POST['semester']
        f=request.FILES['filedoc']
        ft=request.POST['filetype']
        des=request.POST['description']
        to=User.objects.get(username=str(request.POST['to']))
        try:
            Notes.objects.create(user=u,uploadDate=date.today(),subject=s,semester=se,notesFile=f,fileType=ft,description=des,status="Pending",receiverType="Teacher",sendTo=to)
            error="no"
        except:
            error="yes"
    d={'person_obj':person_obj,'user_obj':user_obj,'error':error,'all_usernames':all_usernames}
    return render(request,'s_uploadnotes.html',d)

def s_viewmynotes(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    person_obj=Person.objects.get(user=request.user)
    notes=Notes.objects.filter(user=person_obj)
    d={'notes':notes}
    return render(request,'s_viewmynotes.html',d)

def s_deletemynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('signin')
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('s_viewmynotes')

def s_viewallnotes(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    p=Person.objects.get(user=request.user)
    notes=Notes.objects.filter(receiverType="Student",sendTo=p.batch+"-"+p.branch+"-"+p.section)
    print(p.batch+"-"+p.branch+"-"+p.section)
    d={'notes':notes}
    return render(request,'s_viewallnotes.html',d)
