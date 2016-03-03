"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa.views import bad_route, test

urlpatterns = [
    url(r'^$', bad_route),
    url(r'^login/', bad_route),
    url(r'^signup/', bad_route),
    url(r'^question/(?P<id>[^/]+)', test),
    url(r'^ask/', bad_route),
    url(r'^popular/', bad_route),
    url(r'^new/', bad_route),
    url(r'^admin/', admin.site.urls),
]
