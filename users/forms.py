import profile
from django import forms
from . models import *

class UserProfile(forms.ModelForm):
    password1 = forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label=('Confirm Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Profile
        fields = ['fullname','username','email','password1','password2','profile_picture']
        widgets ={
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class':'form-control','type':'file'})
        }
class UpdateProfile(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Profile
        fields = ['fullname','username','email']
        widgets ={
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
        }
class UpdatePicture(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
        widgets ={
                'profile_picture': forms.FileInput(attrs={'class':'form-control','type':'file'})
            }

# class Company(models.Model):
#     employer = models.OneToOneField(User, on_delete = models.CASCADE)
#     company_name = models.CharField(max_length=250)
#     company_category = models.CharField(max_length=250)
#     language = models.CharField(max_length=250)
#     username = models.CharField(max_length=250)
#     company_website = models.CharField(max_length=50)
#     company_facebook = models.CharField(max_length=250)
#     company_instagram = models.CharField(max_length=250)
#     company_twitter = models.CharField(max_length=250)
#     company_linkedin = models.CharField(max_length=250)
#     company_address = models.CharField(max_length=250)
#     company_city = models.CharField(max_length=250)
#     company_zip = models.CharField(max_length=250)
#     company_country = models.CharField(max_length=250)
#     company_about = models.TextField()
#     email = models.EmailField()
#     company_phone = models.CharField(max_length=50)
#     company_picture = models.ImageField(upload_to="companies/", blank=True, null = True)

#     def __str__(self):
#         return self.company_name

# from django.shortcuts import render,redirect
# from . forms import UserCompany
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth import login,logout,authenticate

# # Create your views here.
# def account(request):

#     return render (request, 'userfiles/accounts.html')
# def create(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     form = UserCompany()
#     if request.method == 'POST':
#         form = UserCompany(request.POST, request.FILES)

#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             password2 = form.cleaned_data.get('password2')
#             email = form.cleaned_data.get('email')

#             if User.objects.filter(username = username):
#                 messages.warning(request,'Username Already exist')
#                 return redirect('create')
#             if User.objects.filter(email = email):
#                 messages.warning(request,'Email Already exist')
#                 return redirect('create')
#             if password != password2:
#                 messages.warning(request,'Password not match')
#                 return redirect('create')

#             user = User.objects.create_user(username,email,password)
#             form = form.save(commit= False)
#             form.user = user
#             form.save()
#             messages.success(request, 'Registration successful !')
#             return redirect('home')
#     context = {
#         'form':form
#     }
#     return render(request, 'userfiles/create.html',context)

# def loginUser(request):
#     if request.user.is_authenticated:
#         return redirect('dashboard')
#     if request.method == 'POST':
#         username = request.POST.get('uname')
#         password = request.POST.get('pwd')

#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful !')
#             return redirect('home')
#         else:
#             messages.warning(request, 'Invalid Username or Password !')
#             return redirect('login')

#     return render(request, 'maxpro/login.html')

# def dashboard(request):
#     if request.user.is_authenticated:
#         profile = request.user.profile
#         # orders = Order.objects.all().filter(id = profile)
#         context = {
#             'profile':profile,
#             # 'orders':orders
#         }
    
#         return render(request, 'maxpro/dashboard.html',context)
#     else:
#         return redirect('login')

# def logoutUser(request):
#     logout(request)
#     messages.success(request, 'Logout successful !')

#     return redirect('login')
# def updateUser(request):
#     user = request.user.profile
#     form = UpdateProfile(instance=user)
#     if request.method == 'POST':
#         form = UpdateProfile(request.POST, instance= user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Update successful !')
#             return redirect('dashboard')

#     context = {
#         'form':form
#     }
#     return render(request, 'maxpro/updateprofile.html',context)

# def updatePicture(request):
#     profile = request.user.profile
#     user = request.user.profile
#     form = UpdateProfile(instance=user)
#     if request.method == 'POST':
#         form = UpdateProfile(request.POST, request.FILES, instance= user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile picture change successful !')
#             return redirect('dashboard')

#     context = {
#         'form':form,
#         'profile':profile
#     }
#     return render(request, 'maxpro/updatepicture.html',context)

#             company = Company(company_name=form.cleaned_data['company_name'], company_category=form.cleaned_data['company_category'], language=form.cleaned_data['language'], company_website=form.cleaned_data['company_website'], company_facebook=form.cleaned_data['company_facebook'], company_instagram=form.cleaned_data['company_instagram'], company_twitter=form.cleaned_data['company_twitter'], company_linkedin=form.cleaned_data['company_linkedin'], company_address=form.cleaned_data['company_address'], company_city=form.cleaned_data['company_city'], company_zip=form.cleaned_data['company_zip'], company_country=form.cleaned_data['company_country'], company_about=form.cleaned_data['company_about'], company_phone=form.cleaned_data['company_phone'], company_picture=form.cleaned_data['company_picture'],)
