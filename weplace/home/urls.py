from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('login/', views.loginmain,name='loginmain'),
    path('studentlogin/', views.studentlogin,name='studentlogin'),
    path('myprofile/', views.myprofile,name='myprofile'),
    path('applystudent/', views.applystudent,name='applystudent'),
    path('studentsignup/', views.studentsignup,name='studentsignup'),
    path('', views.index,name='signout'),  
    path('signup/', views.signup,name='signup'),
    

]