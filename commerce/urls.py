from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('product/<int:pk>',views.product,name='product')
]   
# we created urls for the app and now we need to include this to main urls.py