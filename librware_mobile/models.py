from django.db import models
import datetime
# Create your models here.

class Library(models.Model):
	libraryName = models.CharField(max_length=200) 
	create_date = models.DateTimeField('Date updated') 
	libraryURL = models.URLField(verify_exists=True)
	libraryHash = models.CharField(max_length=20)
	defaultFeed = models.URLField(verify_exists=True)
	defaultSearchBase = models.URLField(verify_exists=True)
	libraryIcon = models.ImageField(upload_to="img")
	defaultFeedIdon = models.ImageField(upload_to="img")
	libraryFooter = models.ImageField(upload_to="img")
	#libraryFooter = models.ImageField(upload_to="img")
	libraryAbout = models.CharField(max_length=500)
	libraryImage = models.ImageField(upload_to="img")
	def __unicode__(self):
		return self.libraryName

class Feed(models.Model):	
	library = models.ForeignKey(Library)
	feedOrder = models.IntegerField()
	feedName = models.CharField(max_length=100)
	feedURI = models.URLField(verify_exists=True)
	def __unicode__(self):
		return self.feedName

class Contact(models.Model):
	library = models.ForeignKey(Library)
	contactOrder = models.IntegerField()
	contactName = models.CharField(max_length=100)
	contactPhone = models.CharField(max_length=30)
	contactEmail = models.EmailField()
	contactSMS = models.CharField(max_length=30)
	contactURI = models.URLField()
	contactDescription = models.CharField(max_length=200)
	def cleaned_phone(contactPhone):
		return contactPhone.translate(None, '()-.')
	def cleaned_sms(contactSMS):
		return contactSMS.translate(None, '()-.')
	def __unicode__(self):
		return self.contactName

class Location(models.Model):
	library = models.ForeignKey(Library)
	locationOrder = models.IntegerField()
	locationName = models.CharField(max_length=200)
	locationURI = models.CharField(max_length=50)
	locationMarkerColor = models.CharField(max_length=10)
	locationMarkerLabel = models.CharField(max_length=10)
	def __unicode__(self):
		return self.locationName

class Hours(models.Model):
	library = models.ForeignKey(Library)
	hoursOrder = models.IntegerField()
	hoursName = models.CharField(max_length=200)
	hoursText1 = models.CharField(max_length=200)
	hoursText2 = models.CharField(max_length=200)
	hoursText3 = models.CharField(max_length=200)
	hoursText4 = models.CharField(max_length=200)
	def __unicode__(self):
		return self.hoursName

class ExternalLinks(models.Model):
	library = models.ForeignKey(Library)
	linkOrder = models.IntegerField()
	linkText = models.CharField(max_length=200)
	linkURI = models.URLField(verify_exists=True)
	def __unicode__(self):
		return self.linkText
