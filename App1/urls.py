
from django.urls import path

from App1 import views

urlpatterns=[
    path('',views.userlogin),
    path('changepsw', views.changepsw),
    path('createprofile', views.createprofile),
    path('detailedview/<int:id>/',views.detailedview),
    path('forgottpsw', views.forgottpsw),
    path('register', views.UserRegister),
    path('resetpsw', views.resetpsw),
    path('updateprofile', views.updateprofile),
    path('Home', views.Home),
    path('viewprofile',views.viewprofile),
    path('edit/updatetask/<int:id>/',views.updatetask),
    path('completedtask',views.completedtask),
    path('Addtask',views.Addtask),
    path('Pendingtask',views.Pendingtask),
    path('delete/<int:id>',views.delete),
    path('add/<int:id>/',views.add)

]