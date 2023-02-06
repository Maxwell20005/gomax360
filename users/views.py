from django.shortcuts import render,redirect
from . forms import UserProfile,UpdateProfile
from django.contrib.auth.models import User
from django.contrib import messages
from stores.models import Order
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = UserProfile()
    if request.method == 'POST':
        form = UserProfile(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')

            if User.objects.filter(username = username):
                messages.warning(request,'Username Already exist')
                return redirect('register')
            if User.objects.filter(email = email):
                messages.warning(request,'Email Already exist')
                return redirect('register')
            if password != password2:
                messages.warning(request,'Password not match')
                return redirect('register')

            user = User.objects.create_user(username,email,password)
            form = form.save(commit= False)
            form.user = user
            form.save()
            messages.success(request, 'Registration successful !')
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'maxpro/registration.html',context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful !')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Username or Password !')
            return redirect('login')

    return render(request, 'maxpro/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        # orders = Order.objects.all().filter(id = profile)
        context = {
            'profile':profile,
            # 'orders':orders
        }
    
        return render(request, 'maxpro/dashboard.html',context)
    else:
        return redirect('login')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Logout successful !')

    return redirect('login')
def updateUser(request):
    user = request.user.profile
    form = UpdateProfile(instance=user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance= user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful !')
            return redirect('dashboard')

    context = {
        'form':form
    }
    return render(request, 'maxpro/updateprofile.html',context)

def updatePicture(request):
    profile = request.user.profile
    user = request.user.profile
    form = UpdateProfile(instance=user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES, instance= user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture change successful !')
            return redirect('dashboard')

    context = {
        'form':form,
        'profile':profile
    }
    return render(request, 'maxpro/updatepicture.html',context)

