from django.conf.urls import url

from django.contrib import admin

from django.urls import path 

from . import views

urlpatterns = [

    path('postsign/',views.postsign),

    path('logout/',views.logout,name="log"),

    path('/',views.home),

    path('postsignup/',views.postsignup,name='postsignup'),

    path('create/',views.create,name='create'),

    path('upload/',views.upload,name='upload'),

    path('post_create/',views.post_create,name='post_create'),

    path('upload_save/',views.upload_save,name='upload_save'),

    path('postsign/dept/',views.departments, name='dept'),

    path('postsign/club/',views.club, name='club'),

    path('postsign/dept/civil/',views.civil, name='civil'),

    path('postsign/dept/mech/',views.mech, name='mech'),

    path('postsign/dept/ece/',views.ece, name='ece'),

    path('postsign/dept/eee/',views.eee, name='eee'),

    path('postsign/dept/mnc/',views.mnc, name='mnc'),

    path('postsign/dept/bio/',views.bio, name='bio'),

    path('postsign/dept/cse/',views.cse, name='cse'),

    path('postsign/dept/chem/',views.chem, name='chem'),

    path('postsign/dept/civil/civcourse/',views.civilcourse, name='civcourse'),

    path('postsign/dept/mech/mccourse/',views.mechcourse, name='mccourse'),

    path('postsign/dept/ece/eccourse/',views.ececourse, name='eccourse'),

    path('postsign/dept/eee/eecourse/',views.eeecourse, name='eecourse'),

    path('postsign/dept/mnc/mnccourse/',views.mnccourse, name='mnccourse'),

    path('postsign/dept/bio/biocourse/',views.biocourse, name='biocourse'),

    path('postsign/dept/cse/csecourse/',views.csecourse, name='csecourse'),

    path('postsign/dept/chem/chemcourse/',views.chemcourse, name='chemcourse'),



]
