from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
import datetime
# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')



@login_required(login_url='login')
@admin_only
def home(request):
	today = datetime.date.today()
	orders = Order.objects.all()
	customers = Customer.objects.all()
	
	total_customers = customers.count()

	total_orders = orders.count()
	Klar = orders.filter(status='Klar').count()
	Ikke_Klar = orders.filter(status='Ikke_Klar').count()
	
	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'Klar':Klar,
	'Ikke_Klar':Ikke_Klar }

	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	orders = request.user.customer.order_set.all()

	total_orders = orders.count()
	Klar = orders.filter(status='Klar').count()
	Ikke_Klar = orders.filter(status='Ikke_Klar').count()
	Ja = orders.filter(VINDUER='Ja').count()
	Nej = orders.filter(VINDUER='Nej').count()
	Yes = orders.filter(STOVSUGE='Yes').count()
	No = orders.filter(STOVSUGE='No').count()
	print('ORDERS:', orders)

	context = {'orders':orders, 'total_orders':total_orders,
	'Klar':Klar,'Ikke_Klar':Ikke_Klar,
	'Ja': Ja, 'Nej': Nej, 'Yes': Yes, 'No': No}
	return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'accounts/account_settings.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()
	order_count = orders.count()

	total_orders = orders.count()
	Klar = orders.filter(status='Klar').count()
	Ikke_Klar = orders.filter(status='Ikke_Klar').count()
	Ja = orders.filter(VINDUER='Ja').count()
	Nej = orders.filter(VINDUER='Nej').count()
	Yes = orders.filter(STOVSUGE='Yes').count()
	No = orders.filter(STOVSUGE='No').count()



	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'Klar':Klar, 'Ikke_Klar':Ikke_Klar, 'Ja': Ja, 'Nej': Nej, 'Yes': Yes, 'No': No, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'accounts/customer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('bus', 'product', 'start_date', 'end_date', 'status'), extra=30 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)






@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def cross_off(request, list_id):
	order = Order.objects.get(pk=list_id)
	order.status = 'Ikke_Klar'
	order.save()
	return redirect('/')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def uncross(request, list_id):
	order = Order.objects.get(pk=list_id)
	order.status = 'Klar'
	order.save()
	return redirect('/')


