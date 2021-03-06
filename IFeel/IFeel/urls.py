"""IFeel URL Configuration

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
from django.urls import path, include

from IFeel import view

questionary_urls = [
    path('create/<int:template_id>/', view.MakeQuestionaryView.as_view(), name='make_questionary'),
    path('update/<int:questionary_id>/', view.UpdateQuestionaryView.as_view(), name='update_questionary'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('templates/', view.TemplatesView.as_view(), name="templates"),
    path('questionary/', include(questionary_urls)),
]
