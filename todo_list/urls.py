from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('vaskelist/', views.vaskelist, name='vaskelist'),
	path('larsenbus/', views.larsenbus, name='larsenbus'),
	path('index/', views.index, name='index'),
	path('delete/<list_id>', views.delete, name='delete'),
	path('cross_off/<list_id>', views.cross_off, name='cross_off'),
	path('uncross/<list_id>', views.uncross, name='uncross'),
	path('edit/<list_id>', views.edit, name='edit'),

]
