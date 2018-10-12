from django.urls import path, include
from riverrapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('loginout/', auth_views.login,name='login'),
    path('login/', auth_views.logout,name='logout'),
    path('my_gigs/',views.my_gigs,name = 'my_gigs'),
    path('create_gig/',views.create_gig,name = 'create_gig'),
]