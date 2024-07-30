from django.shortcuts import render,redirect
from  .forms import RegistrationForm,ChangeUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
from django.urls  import reverse_lazy
from django.views.generic import CreateView,DetailView,UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from order.models import  Order
from car.models import Car

# Create your views here.
class UserSignupView(CreateView):
    template_name='register.html'
    form_class = RegistrationForm
    def get_success_url(self):
        return reverse_lazy('register')

    def form_valid(self, form):
        messages.success(self.request, "Registration successfull")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Please Enter valid information")
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['type'] = 'Register'
          return context  
     
class UserLoginView(LoginView):
    template_name='register.html'
    def get_success_url(self):
        return reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, "Logged in Successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Please Enter valid information")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['type'] = 'Log In'
          return context 

# profile view
@method_decorator(login_required, name='dispatch')
class ProfileView(CreateView):
    template_name='profile.html'
    model=User
    context_object_name = 'user_data'
    fields=['username','first_name','last_name','email']
   
    def get_object(self):
      return self.request.user
   
    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['orders'] = Order.objects.filter(user=self.request.user)
          context['user_data'] = self.get_object() 
          return context  

# edit profile

@method_decorator(login_required,name='dispatch')
class EditProfileView(UpdateView):
    template_name='register.html'
    model=User
    form_class =ChangeUserForm

    context_object_name = 'user_data' # Change the context object name
    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self):
        return self.request.user
#    currebtly user object fetch

    def form_valid(self, form):
        messages.success(self.request, "Profile Updated Successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Please Enter valid information")
        return super().form_invalid(form)    

    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['type'] = 'Update Profile'
         
          return context        



# edit password
@method_decorator(login_required,name='dispatch')
class EditPasswordView(PasswordChangeView):
    template_name='register.html'
   
    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Password Change Successful")
        return super().form_valid(form)
 
    def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['type'] = 'Edit Password'
         
          return context
    
# logout
# @method_decorator(login_required,name='dispatch')
# class UserLogoutView(LogoutView):
#      def get_success_url(self):
#         messages.success(self.request, 'Logged out successfully')
#         return reverse_lazy('login')


def user_logout(request):
     
     logout(request)
     messages.success(request,'Logged Out Successfully')
    
     return redirect('login')     

@login_required
def Buynow(request,id):
    car=Car.objects.get(pk=id)
    if car.quantity>0:
        car.quantity-=1
        messages.success(request,'Car Buy Successfully')
        car.save()
        Order.objects.create(user=request.user,car=car)
    else:
        messages.warning(request,'Sorry The Car stock out')
    return redirect("profile")       
