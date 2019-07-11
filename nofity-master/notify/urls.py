"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from notifyapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('url', views.uurll),
    path('show',views.show),
    path('editURL/<int:id>', views.update),
    path('deleteURL/<int:id>', views.destroy),

    path('cat', views.catg),
    path('showCat', views.showc),
    path('editC/<int:id>', views.updatec),
    path('deleteC/<int:id>', views.destroyc),

]