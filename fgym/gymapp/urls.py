from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='Home'),
    path('Trainer', views.trainer, name='trainer'),
    path('Why-Us', views.whyus, name='whyus'),
    path('Contact', views.contact, name='contact'),
    
    
]
