# path('register/', RegistrationView.as_view(), name='register'),
#     path('profile/', ProfileView.as_view(), name='profile'),
from django.conf.urls import url
from django.urls import path

from users.views import ProfileView, RegistrationView
app_name ='users'

urls =[
    # url(r'^', include(router.urls)),

    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]