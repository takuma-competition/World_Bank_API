"""World_Statistics_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

#アプリの名前が必要らしいけどなぜ必要かよくわからん
app_name = 'Country_population'

#解説参考：https://www.nblog09.com/w/2019/02/09/django-template-url/

urlpatterns = [
    path('', views.index, name='index'),
    path('plot/', views.get_svg, name='plot')
]
