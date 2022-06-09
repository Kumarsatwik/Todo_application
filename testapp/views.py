from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import UserCreationForm
from testapp.models import *
from testapp.forms import TodoForm
import random
import uuid
#  Create your views here.

def index(request):
	login=request.session.get('user')
	msg=False
	data=None
	if login:
		login=uuid.UUID(login).hex
		u_data=user.objects.get(id=login)
		data=Todo.objects.filter(user=u_data)
		msg=True
	form=TodoForm()
	return render(request,'index.html',context={'form':form,'msg':msg,'data':data})


def add_todo(request):
	login=request.session.get('user')
	if login:
		login=uuid.UUID(login).hex
		data=user.objects.get(id=login)
		form=TodoForm(request.POST)
		if form.is_valid():
			todo=form.save(commit=False)
			todo.user=data
			todo.serial=uuid.uuid4
			todo.save()	
			return redirect('home')
		else:
			return redirect('home')
	else:
		return redirect('login')

def remove(request,slug):
	try:
		data=Todo.objects.get(title=slug)
		data.delete()
		return redirect('home')
	except:
		print("Something went wrong")
		return redirect('home')


def login(request):
	login=request.session.get('user')
	if login:
		return redirect('home')
	else:
		if request.method == 'POST':
			email=request.POST.get('email')
			password=request.POST.get('password')
			try:
				data=user.objects.get(email=email)
			except:
				data=False
			if data:
				check=check_password(password,data.password)
				if check:
					request.session['user']=str(data.id)
					request.session['email']=data.email
					return redirect('home')
				else:
					error_msg="Password is incorrect"
					return render(request, 'login.html',{'error_msg':error_msg})
			else:
				error_msg="Email Not Found"
				return render(request, 'login.html',{'error_msg':error_msg})
	return render(request,'login.html')	

def logout(request):
	request.session.clear()
	return redirect('home')

def signup(request):
	signup=request.session.get('user')
	if not signup:
		if request.method=="POST":
			name=request.POST.get('name')
			password=request.POST.get('password')
			email=request.POST.get('email')
			error_msg=None
			if email.find("@")==-1:
				error_msg="Invalid Email address"
			elif len(password)<8:
				error_msg="Password must be at least 8 characters"
			elif user.objects.filter(email=email).exists():
				error_msg="Email address already exists"

			if not error_msg :
				data = user(name=name,password=password,email=email)
				data.password = make_password(data.password)
				data.save()
				return redirect('home')
			else:
				error={
					'error':error_msg
				}
				return render(request, 'signup.html',error)
	else:
		return redirect('home')
	return render(request, 'signup.html')