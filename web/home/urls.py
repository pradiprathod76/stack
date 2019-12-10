from django.urls import path
from .views import home, single_post,Develop,Print,Design
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home,name='home'),
    path('develop',Develop,name='develop'),
    path('print',Print,name='print'),
    path('design',Design,name='design'),
    path('single_post/<int:id>', single_post , name='single_post'),

    
] 

