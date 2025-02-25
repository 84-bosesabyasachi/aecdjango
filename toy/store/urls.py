from django.urls import path
from .views import signup,myaction,show,dele,edit,upd,login,userlogin,approve,decline

urlpatterns=[
    path('signup',signup,name='signup'),
    path('myaction',myaction,name='myaction'),
    path('show',show,name='show'),
    path('dele/<int:id>',dele),
    path('upd/<int:id>',upd),
    path('edit/<int:id>',edit),
    path('approve/<int:id>',approve),
    path('decline/<int:id>',decline),
    path('login',login,name='login'),
    path('userlogin',userlogin,name='userlogin'),
]