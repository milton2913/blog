from django.shortcuts import render
from django.contrib import messages
from apps.blog.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message has been sent successfully!')
            return render(request, 'pages/contact.html', {'form': ContactForm()})
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})
