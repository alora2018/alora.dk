from django.shortcuts import render, redirect
from .models import Vaskelist 
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponse
from django.template import Context, loader
from datetime import date
from django.utils.timezone import now
import datetime

def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = Vaskelist.objects.all
			messages.success(request, ('Bus og Program er tastet ind!'))
			return render(request, 'home.html', {'all_items': all_items})

	else:
		all_items = Vaskelist.objects.all
		return render(request, 'home.html', {'all_items': all_items})

def about(request):
	context = {'first_name': 'John', 'last_name': 'Elder'}
	return render(request, 'about.html', context)
	
def vaskelist(request):
			today = datetime.date.today()
			all_items = Vaskelist.objects.all().filter(end_date__gte=date.today())		
			return render(request, 'vaskelist.html', {'all_items': all_items})

def index(request):
			today = datetime.date.today()
			all_items = Vaskelist.objects.all().filter(start_date__gte=datetime.date.today(), \
			end_date__lte=datetime.date.today() + datetime.timedelta(hours=24))

			return render(request, 'index.html', {'all_items': all_items})


def larsenbus(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = Vaskelist.objects.all
			messages.success(request, ('Bus og Program er tastet ind!'))
			return render(request, 'larsenbus.html', {'all_items': all_items})

	else:
		all_items = Vaskelist.objects.all
		return render(request, 'larsenbus.html', {'all_items': all_items})



def delete(request, list_id):
	bus = Vaskelist.objects.get(pk=list_id)
	bus.delete()
	messages.success(request, ('Bus er slettet fra listen!'))
	return redirect('home')

def cross_off(request, list_id):
	bus = Vaskelist.objects.get(pk=list_id)
	bus.completed = True
	bus.save()
	return redirect('vaskelist')

def uncross(request, list_id):
	bus = Vaskelist.objects.get(pk=list_id)
	bus.completed = False
	bus.save()
	return redirect('vaskelist')

def edit(request, list_id):
	if request.method == 'POST':
		bus = Vaskelist.objects.get(pk=list_id)

		form = ListForm(request.POST or None, instance=bus)

		if form.is_valid():
			form.save()
			messages.success(request, ('Bus/Program er blevet redigeret!'))
			return redirect('home')

	else:
		bus = Vaskelist.objects.get(pk=list_id)
		return render(request, 'edit.html', {'bus': bus})

