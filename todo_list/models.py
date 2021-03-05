from django.db import models
from django.contrib.auth.models import User

  
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Udvendig', 'Udvendig'),
			('Udvendig + tank', 'Udvendig + tank'),
			('Indvendig + Støvsuges', 'Indvendig + Støvsuges'),
			('Indvendig + Støvsuges + Vinduer', 'Indvendig + Støvsuges + Vinduer'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Ikke_klar', 'Ikke_klar'),
			('Klar', 'Klar'),
			)

	STOVSUGE = (
			('Ja', 'Ja'),
			('Nej', 'Nej'),
			)

	VINDUER = (
			('Ja', 'Ja'),
			('Nej', 'Nej'),
			)

	BUS_CHOICES = ( 
	("", "Valg bus!"),
	("Dania 00", "Dania 00"), 
	("Dania 1", "Dania 1"), 
	("Dania 2", "Dania 2"), 
	("Dania 3", "Dania 3"), 
	("Dania 4", "Dania 4"), 
	("Dania 5", "Dania 5"), 
	("Dania 6", "Dania 6"), 
	("Dania 7", "Dania 7"), 
	("Dania 8", "Dania 8"), 
	("Dania 9", "Dania 9"), 
	("Dania 10", "Dania 10"), 
	("KBH 50", "KBH 50"), 
	("KBH 51", "KBH 51"), 
	("KBH 52", "KBH 52"), 
	("KBH 53", "KBH 53"), 
	("KBH 54", "KBH 54"), 
	("KBH 55", "KBH 55"), 
	("KBH 56", "KBH 56"), 
	("KBH 57", "KBH 57"), 
	("KBH 58", "KBH 58"), 
	("KBH 59", "KBH 59"), 
	("KBH 60", "KBH 60"), 
	("KBH 61", "KBH 61"), 
	("KBH 62", "KBH 62"), 
	("KBH 63", "KBH 63"), 
	("KBH 64", "KBH 64"), 
	("KBH 65", "KBH 65"), 
	("KBH 66", "KBH 66"), 
	("KBH 67", "KBH 67"),
	("KBH 68", "KBH 68"),
	("KBH 69", "KBH 69"),
	("KBH 70", "KBH 70"),
	("KBH 71", "KBH 71"),
	("KBH 72", "KBH 72"),
	("KBH 73", "KBH 73"),
	("KBH 74", "KBH 74"),
	("KBH 75", "KBH 75"),
	("KBH 76", "KBH 76"),
	("KBH 77", "KBH 77"),
	("KBH 78", "KBH 78"),
	("KBH 79", "KBH 79"),
	("KBH 80", "KBH 80"),
	("KBH 81", "KBH 81"),
	("KBH 82", "KBH 82"),
	("KBH 83", "KBH 83"),
	("KBH 84", "KBH 84"),
	("KBH 85", "KBH 85"),
	("KBH 86", "KBH 86"),
	("KBH 87", "KBH 87"),
	("KBH 88", "KBH 88"),
	("KBH 89", "KBH 89"),
	("KBH 90", "KBH 90"),
	("KBH 91", "KBH 91"),
	("KBH 92", "KBH 92"),
	("KBH 93", "KBH 93"),
	("KBH 94", "KBH 94"),
	("FLIXBUS-1", "FLIXBUS-1"),
	("FLIXBUS-2", "FLIXBUS-2"),
	("NY DD1", "NY DD1"),
	("NY DD2", "NY DD2"),

	)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	bus = models.CharField(max_length=200, choices = BUS_CHOICES, 
    default = '')
	status = models.CharField(max_length=200, null=True, blank=True,  choices=STATUS)
	stovsuge = models.CharField(max_length=200, null=True, blank=True,  choices=STOVSUGE)
	vinduer = models.CharField(max_length=200, null=True, blank=True,  choices=VINDUER)
	start_date = models.DateTimeField(blank=True, null=True)
	end_date = models.DateTimeField(blank=True, null=True)
	note = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.bus + ' | ' + str(self.status)