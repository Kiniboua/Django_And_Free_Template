from django.urls import path 
from .import views

urlpatterns = [
    path ('', views.home, name="home"),
   # path ('home.html', views.home, name="home"),
    path('about.html', views.aboutview, name="about"),
    path('blog-single.html', views.blogsingleview, name="blog-single"),
    path('blog.html', views.blogview, name="blog"),
    path('contact.html', views.contactview, name="contact"),
    path('doctors.html', views.doctorsview, name="doctors"),
    path('services.html', views.servicesview, name="sercices"),

]
