from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('restaurents',views.restaurents, name='restaurents'),
    path('about_us',views.about_us, name='about_us'),
    path('partner', views.partner, name='partner'),
    path('job', views.jobs, name='job'),
    path('stories', views.stories, name='stories'),
    path('register', views.register, name='register'),
    path('details', views.details, name='details'),
    path('menu/<rid>',views.menu_, name='menu'),
    path('billing',views.billing,name="billing")
]