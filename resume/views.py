from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request,"about.html")

def projects (request):
     projects_show = [
    {
        'title': 'Watch Store',
        'path': 'images/watch.png',
        'description': 'An e-commerce web application for watches with product listing, cart functionality, and user-friendly UI built using Django.',
          
        'github_link': 'https://muralivarma13.github.io/css-project1/'
    },
    {
        'title': 'Password Generator',
        'path': 'images/password.png',
        'description': 'A Python-based password generator that creates strong and secure passwords based on user-defined criteria.',
        'github_link': 'https://muralivarma13.github.io/js-project1/'
    },
    {
        'title': 'Movie App',
        'path': 'images/movieapp.png',
        'description': 'A movie browsing application that displays movie details, ratings, and categories using Django and external APIs.',
        'github_link': 'https://muralivarma13.github.io/movieapp-jsproject/'
    },
    {
        'title': 'Ecommerce',
        'path': 'images/Ecommerce.png',
        'description': 'A full-featured e-commerce application with CRUD operations, product management, and database integration using Django.',
        'github_link': 'https://simple-mart-react-project.vercel.app/'
    },
   
]
  

   
     return render (request,"projects.html",{"projects_show": projects_show})


def experience(request):
    experience = [
    {
        "company": "Academic Projects",
        "position": "Python Django Developer (Fresher)"
    },
    {
        "company": "Self Learning",
        "position": "Python Full Stack Learner"
    },
    {
        "company": "Online Training",
        "position": "Django & REST Framework Learner"
    }
]

    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)