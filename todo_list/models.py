from django.db import models
from datetime import datetime
from django.utils import timezone
PROGRAM_CHOICES = ( 
	("", "Valg program!"),
    ("Program 1", "1"), 
    ("Program 2", "2"), 
    ("Program 3", "3"), 
    ("Program 4", "4"), 
  
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

class Vaskelist(models.Model):
	timestamp = models.DateField(default=timezone.now)
	bus = models.CharField(max_length=200, choices = BUS_CHOICES, 
    default = '')
	Program = models.CharField(max_length=200, choices = PROGRAM_CHOICES, 
    default = '0')
	Kommentar = models.CharField(blank=True, max_length=200)
	completed = models.BooleanField(default=False)
	start_date = models.DateTimeField(blank=True, null=True)
	end_date = models.DateTimeField(blank=True, null=True)
	def __str__(self):
		return self.bus + ' | ' + str(self.completed)

