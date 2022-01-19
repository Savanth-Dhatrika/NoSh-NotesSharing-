
from os import name
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('signin',signin,name='signin'),
    path('signup',signup,name='signup'),
    path('signout',signout,name='signout'),
    path('teacher_login',teacher_login,name='teacher_login'),
    path('teacher_home',teacher_home,name='teacher_home'),
    path('student_home',student_home,name='student_home'),
    path('s_changepassword',s_changepassword,name='s_changepassword'),
    path('s_editprofile',s_editprofile,name='s_editprofile'),
    path('s_uploadnotes',s_uploadnotes,name='s_uploadnotes'),
    path('s_viewmynotes',s_viewmynotes,name='s_viewmynotes'),
    path('s_deletemynotes/<int:pid>',s_deletemynotes,name='s_deletemynotes'),
    path('s_viewallnotes',s_viewallnotes,name='s_viewallnotes'),
    path('t_viewusers',t_viewusers,name='t_viewusers'),
    path('t_uploadnotes',t_uploadnotes,name='t_uploadnotes'),
    path('t_deleteusers/<int:pid>',t_deleteusers,name='t_deleteusers'),
    path('t_pendingnotes',t_pendingnotes,name='t_pendingnotes'),
    path('t_assignstatus/<int:pid>',t_assignstatus,name='t_assignstatus'),
    path('t_acceptednotes',t_acceptednotes,name='t_acceptednotes'),
    path('t_rejectednotes',t_rejectednotes,name='t_rejectednotes'),
    path('t_allnotes',t_allnotes,name='t_allnotes'),
    path('t_deletenotes/<int:pid>',t_deletenotes,name='t_deletenotes')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
