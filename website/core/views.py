from django.shortcuts import render
import pyrebase
from django.contrib import auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
config = {
    'apiKey': "AIzaSyDacvxdaPmR8qgOqHWXSFKYqJQP1aaDae0",
    'authDomain': "kritiapp-2f73b.firebaseapp.com",
    'databaseURL': "https://kritiapp-2f73b.firebaseio.com",
    'projectId': "kritiapp-2f73b",
    'storageBucket': "kritiapp-2f73b.appspot.com",
    'messagingSenderId': "924829656507",
    'appId': "1:924829656507:web:753c82b560e4a375d1d09e",
  'measurementId': "G-13JKYMC09Z"
  }

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.
def home(request):
    return render(request,'home.html')

def postsign(request):     #login with credentials
    email = request.POST.get('email')
    password = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email,password)
    except:
        message = "invalid credentials..Try signing up"           # if wrong credentials returns to home page
        return render(request, "home.html", {"msg":message})

    if email in ['cse@iitg.ac.in','eee@iitg.ac.in','codingclub@iitg.ac.in','finance@iitg.ac.in']:
        user_id = user['localId']
        name = database.child('ClubDept').child(user_id).child("name").get()
        all_courses = database.child(name.val()).child("courses").get()

        courses=[]
        count=0
        try:
            for course in all_courses:
                courses.append(str(count)+" "+course.key())
                count+=1
        except:
            pass
        session_id=user['idToken']
        request.session['user_id'] = str(session_id)
        return render(request,'upload.html',{"name": name.val(), "courses": courses})

    else:
        user_id = user['localId']
        name = database.child('Users').child(user_id).child("name").get()
        session_id = user['idToken']
        request.session['user_id'] = str(session_id)
        return render(request, "index.html", {"name": name.val()} )

def upload(request):
    idtoken= request.session['user_id']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    user_id = a['localId']
    name = database.child("Users").child(user_id).child("name").get()
    return render(request, "upload_common.html", {"name": name.val()})

def logout(request):
    auth.logout(request)
    return render(request,'home.html')
