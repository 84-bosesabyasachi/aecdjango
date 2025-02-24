from django.urls import path
from .views import signup,myaction,show,dele

urlpatterns=[
    path('signup',signup,name='signup'),
    path('myaction',myaction,name='myaction'),
    path('show',show,name='show'),
    path('dele/<int:id>',dele)
]