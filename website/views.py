from django.shortcuts import render
from django.core.mail import send_mail



def home(request):
    return render(request, 'home.html', {})


def aboutview(request):
    return render(request, 'about.html', {})


def blogsingleview(request):
    return render(request, 'blog-single.html', {})


def blogview(request):
    return render(request, 'blog.html', {})




def contactview(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_subject = request.POST['message_subject']
        message = request.POST['message']

        # Send an email
        send_mail(
            message_subject,
            message,
            'from@example.com',  # Remplace par l'email de l'expéditeur
            ['to@example.com'],  # Remplace par l'email du destinataire
            fail_silently=False,
        )
    
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})



   


def doctorsview(request):
    return render(request, 'doctors.html', {} )

def servicesview(request):
    return render(request, 'services.html', {} )
 