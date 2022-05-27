from django.urls import path
from .views import signupview, signinview, signoutview

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('signin/', signinview, name='signin'),
    path('signout/', signoutview, name='signout'),
]