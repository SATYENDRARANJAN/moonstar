from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from users.forms import RegistrationForm
from users.models import User


class RegistrationView(CreateView):
    template_name ='registration/register.html'
    form_class = RegistrationForm

    def context_data(self,*args,**kwargs):
        context = super(RegistrationView,self).get_context_data(*args,**kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)
        return success_url


class ProfileView(UpdateView):
    model = User
    fields = ['email','phone','password','is_active','is_superuser']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user