from __future__ import unicode_literals
import re
from django.db import models
from datetime import datetime

ALL_LETTERS_REGEX = re.compile(r'[A-Za-z]+')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
      
        if len(postData['name']) < 3: 
            errors['name_length'] = 'Name should be more than 3 characters'
        else:
            if not postData['name'].isalpha():
                errors['name_letters'] = 'Name should be letters only'

        if len(postData['username']) < 3:      
            errors['username'] = 'Username should be more than 3 characters'      

        if len(postData['password']) < 8:
            errors['password_length'] = 'Password needs to be at least 8 characters'
        else:
            if postData['password'] != postData['confirm_password'] :
                errors['confirm_password'] = 'Passwords do not match'
        print "ERRORS", errors

        return errors

class TripManager(models.Manager):
	def basic_validator(self, postData):
		errors  = {}
		# now = datetime.datetime.now()

		if len(postData['destination']) == 0: 
			errors['destination'] = 'Destination name should be longer than 0'     
		elif len(postData['description']) == 0: 
			errors['description'] = 'Description should be longer than 0'      
		# if postData['start_date'] < now:
		# 	errors['start_date'] = "Start date should be after current date"
		# elif postData['end_date'] < now:	
		# 	errors['end_date'] = "End date should be after current date"
		elif postData['end_date']<postData['start_date']:
			errors['date_range'] = "End date should be after start date"
		print 'ERRORS', errors
        
		return errors	

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # joined_trips = models.ManyToManyField(Trip, related_name='joined_users')
    objects = UserManager()	

class Trip(models.Model):
	destination = models.CharField(max_length=255)
	description = models.CharField(max_length=255, default='Description')
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, related_name='joined_trips')
	joined_users = models.ManyToManyField(User, related_name='joined_trips')
	objects = TripManager()

  








