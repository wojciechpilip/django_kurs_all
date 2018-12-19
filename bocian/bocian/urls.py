"""bocian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from blog.views import index, index_temp, details, wpisy_taga, details_with_form, details_with_form_model_form

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', index, name='wpisy-main'),
    path('testtemplate', index_temp),
    path('blog/wpisy/<id_wpisu>', details, name='szczegoly-wpisu'),
    path('blog/wpisy2/<id_wpisu>', details_with_form, name='szczegoly-wpisu2'),  # użycie forms.Form
    path('blog/wpisy3/<id_wpisu>', details_with_form_model_form, name='szczegoly-wpisu3'),  # użycie forms.Form
    path('blog/wpisy/tag/<nazwa_taga>', wpisy_taga, name='wpisy-po-tagu')

]
