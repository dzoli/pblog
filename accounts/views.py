from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm  # it is built-in form
    success_url = reverse_lazy('login')  # redirect user to login page after registration
    template_name = 'signup.html'

# why we use reverse_lazy instead of reverse?
# for all generic class-based views urls are not loaded when file is imported
# we have to use lazy to load them later when they're available
