from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.conf import settings
from .forms import UserRegistrationForm, UserLoginForm
from .utils import send_activation_email
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False # Deactivate until verified
            user.save()
            
            # Send activation email
            try:
                send_activation_email(user, request)
                messages.success(request, 'Registration successful! Please check your email to complete registration.')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
                # Optional: Delete user if email fails? Or let them retry?
                # For now, keep user but they can't login

            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.role = User.Role.USER # Explicitly assign User role (though duplicate default)
        user.save()
        login(request, user)
        messages.success(request, 'Your account has been activated successfully!')
        return redirect('blog:home')
    else:
        return render(request, 'accounts/activation_invalid.html')

class CustomLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('blog:home')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')
