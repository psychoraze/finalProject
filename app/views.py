from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView
from django.views import View
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def team(request):
    return render(request, 'team.html')

def bolide(request):
    return render(request, 'bolide.html')

def admin(request):
    return render(request, 'admin.html')

def racer(request):
    return render(request, 'racer.html')

class RacerCreate(CreateView):
    model = Racer
    form_class = Racer_Form
    success_url = reverse_lazy('home')
    template_name = 'create.html'

class RacerDelete(DeleteView):
    model = Racer
    success_url = reverse_lazy('home')
    template_name = 'delete.html'

class TeamCreate(CreateView):
    model = Team
    form_class = Team_Form
    success_url = reverse_lazy('home')
    template_name = 'create.html'

class BolideCreate(CreateView):
    model = Bolide
    form_class = Bolide_Form
    success_url = reverse_lazy('home')
    template_name = 'create.html'

class AdminCreate(CreateView):
    model = Admin
    form_class = Admin_Form
    success_url = reverse_lazy('home')
    template_name = 'create.html'

class RacerView(DetailView):
    model = Racer
    template_name = 'view.html'
    
    def get_racers(self, **kwargs):
        racers = super().get_context_data(**kwargs)
        racers['form'] = Racer_Form
        racers['racers'] = Racer_Form.objects.all(id=kwargs['pk'])
        return racers

class TeamView(DetailView):
    model = Team
    template_name = 'view.html'

    def get_teams(self, **kwargs):
        teams = super().get_context_data(**kwargs)
        teams['form'] = Team_Form
        teams['teams'] = Team_Form.objects.all(id=kwargs['pk'])
        return teams

class BolideView(DetailView):
    model = Bolide
    template_name = 'view.html'

    def get_bolides(self, **kwargs):
        bolides = super().get_context_data(**kwargs)
        bolides['form'] = Bolide_Form
        bolides['bolides'] = Bolide_Form.objects.all(id=kwargs['pk'])
        return bolides

class RacersList(ListView):
    model = Racer
    template_name = 'view_racers.html'
    context_object_name = 'racers'

class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    success_message = 'Account created successfully'
    
    def send_verification_email(self, user):
        token = default_token_generator.make_token(user)
        verify_url = self.request.build_absolute_uri(f'/verify/{user.pk}/{token}/')
        subject = 'Verify your email'
        message = f'Hello {user.username}, please click the link below to verify your email:\n\n{verify_url}'
        send_mail(subject, message, 'psychorazed@example.com', [user.email])

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object  
        user.is_active = False
        user.save()
        self.send_verification_email(self.object)
        return response
    
class VerifyEmailView(View):
    def get(self, request, user_pk, token):
        user = User.objects.get(pk=user_pk)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your email has been verified')
            return redirect('home')
        else:
            messages.error(request, 'Invalid verification link')
            return redirect('home')
        
class Login(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')
    success_message = 'You are logged in successfully'
    
class Logout(LogoutView):
    next_page = reverse_lazy('home')