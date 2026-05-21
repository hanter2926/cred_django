import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import EmailOTP

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('register')

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name
            )

            otp = str(random.randint(100000, 999999))

            EmailOTP.objects.create(user=user, otp=otp)

            send_mail(
                'Your OTP Verification Code',
                f'Your OTP is {otp}',
                'noreply@ecommerce.com',
                [email],
                fail_silently=False,
            )

            request.session['user_id'] = user.id
            return redirect('verify_otp')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def verify_otp_view(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        user_id = request.session.get('user_id')

        user = User.objects.get(id=user_id)
        otp_obj = EmailOTP.objects.get(user=user)

        if otp_obj.otp == entered_otp:
            otp_obj.is_verified = True
            otp_obj.save()

            send_mail(
                'Welcome to Our Ecommerce Website',
                f'Hello {user.first_name}, welcome to our website!',
                'noreply@ecommerce.com',
                [user.email],
                fail_silently=False,
            )

            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Invalid OTP")

    return render(request, 'accounts/verify_otp.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            otp_obj = EmailOTP.objects.filter(user=user, is_verified=True).first()

            if otp_obj:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Please verify your email first")
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
