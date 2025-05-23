"""
URL configuration for foodtasker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_view
from coreapp import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    # path('', include('googleauthentication.urls')),
    path('accounts/', include('allauth.urls')),
    path('/', include('coreapp.urls')),
    
    
    path('restaurant/sign_in/',auth_view.LoginView.as_view(template_name = 'restaurant/sign_in.html') , name = 'restaurant_sign_in'),
    path('restaurant/sign_out/',auth_view.LogoutView.as_view(next_page = '/') , name = 'restaurant_sign_out'),
    path('restaurant/sign_up', views.restaurant_sign_up, name = 'restaurant_sign_up'),

    
    path('restaurant/', views.restaurant_home, name = 'restaurant_home'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


