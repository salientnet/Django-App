from django.shortcuts import render

from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from .forms import UserForm
from .models import User
from .utils import eligible, bizzfuzz

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_list')

class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/edit.html'
    success_url = reverse_lazy('user_list')

class UserDelete(DeleteView):
	model = User
	success_url = reverse_lazy('user_list')

class UserList(ListView):
    model = User
    template_name = 'users/list.html'

class UserDetail(DetailView):
    model = User
    template_name = 'users/detail.html'

def csv_export(request):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=userlist.csv'
    writer = csv.writer(response)
    writer.writerow([smart_str("Name"), smart_str("Birthday"), smart_str("Eligible"), smart_str("Random Number"), smart_str("BizzFuzz"),])
    users = User.objects.all()
    for user in users:
    	eligible_value = 'allowed' if eligible(user.birthday) else 'blocked'
        writer.writerow([user.username, user.birthday, eligible_value, user.random_number, bizzfuzz(user.random_number),])
    return response
