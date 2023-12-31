from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
  records = Record.objects.all()
  # Check to see if loggin in
  if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      # Authenticate
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          messages.success(request, "You have been logged...")
          return redirect('home')
      else:
          messages.success(request, "Something was wrong")
          return redirect('home')
  else:
      return render(request, 'home.html', {'records': records})
# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out... se you soon")
    return redirect('home')

def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      # Authenticate and login
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, "You Have Successfully Registered! Welcome!")
      return redirect('home')
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form':form})

  return render(request, 'register.html', {'form':form})


def costumer_record(request, pk):
  if request.user.is_authenticated:
    # look up records
    costumer_record = Record.objects.get(id=pk)
    return render(request, 'record.html', {'costumer_record': costumer_record})
  else:
    messages.success(request, "No puedes acceder a la informacion")
    return redirect('home')


def delete_record(request, pk):
  if request.user.is_authenticated:
    delete_it = Record.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "You have deleted a record")
    return redirect('home')
  else:
    messages.success(request, "You must be log so delete that")
    return redirect('home')

def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
        
def update_record(request, pk):
  if request.user.is_authenticated:
      current_record = Record.objects.get(id=pk)
      form = AddRecordForm(request.POST or None, instance=current_record)
      if form.is_valid():
          form.save()
          messages.success(request, "Yup....")
          return redirect('home')
      return render(request, 'update_record.html', {'form':form})
  else:
    messages.success(request, "You Must Be Logged In...")
    return redirect('home')
