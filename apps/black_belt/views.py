
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime

def index(request):
	return render(request, 'black_belt/index.html')

def add_user(request):
    
	print 'ADD USER', request.POST
	errors = User.objects.basic_validator(request.POST)

	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect ('/')	
	else:
		hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(name=request.POST['name'], username = request.POST['username'], password = hash1)
		user.save()
	return redirect('/')

def login(request):
	print 'LOGIN ACTIVE'
	if request.method == 'POST':
		user = User.objects.filter(username=request.POST['username'])
		# if user not found
		if len(user) == 0:
			errors = {}
			errors['username_not_found'] = 'Username not found in our records'
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/')
		else:
			# username on file
			hashed_password = user[0].password
			if bcrypt.checkpw( request.POST['password'].encode(), hashed_password.encode()):
				request.session['name']= user[0].name
				# request.session['username']= user[0].username
				request.session['id'] = user[0].id
				request.session['login'] = True
				return redirect('/travels')
			else:
				errors = {}
				errors['password_no_match'] = 'Incorrect password'
				for tag, error in errors.iteritems():
					messages.error(request, error, extra_tags=tag)
	return redirect('/')

def travels_dashboard(request):
	if 'login' not in request.session:
		return redirect('/')
	if request.session['login']==False:
		return redirect('/')
	print 'GO TO TRAVELS DASHBOARD'
	data = {
		'trips': Trip.objects.all(),
	}
	return render(request, 'black_belt/travels.html', data)

def display_destination_dashboard(request, id):
	if 'login' not in request.session:
		return redirect('/')
	if request.session['login']==False:
		return redirect('/')
	print 'GO TO DISPLAY DESTINATION DASHBOARD' 
	trip = Trip.objects.filter(id=id)
	user = User.objects.filter()
	data = {
	'trip': trip[0],
	'users': User.objects.filter(id = id)
	}
	return render(request, 'black_belt/destination.html', data)		

def travels_add_dashboard(request):
	if 'login' not in request.session:
		return redirect('/')
	if request.session['login']==False:
		return redirect('/')
	print 'GO TO TRAVELS ADD DASHBOARD'
	return render(request, 'black_belt/add.html')  		

def add_trip(request):
	print 'NEW TRIP'
	if request.method == 'POST':
		# errors = Trip.objects.basic_validator(request.POST)
		# if len(errors) == 0:
			trip = Trip.objects.create(destination=request.POST['destination'], description =request.POST['description'], start_date=request.POST['start_date'], end_date=request.POST['end_date'])	
			trip.save()
			# now = datetime.now()
			user = User.objects.get(id=request.session['id'])
			return redirect ('/travels/'+str(trip.id))
	# 	else:
	# 		for tag, error in errors.iteritems():
	# 			messages.error(request, error, extra_tags=tag)
	# return redirect ('/add_trip')	

def logout(request):
	request.session.clear()
	return redirect('/')			




