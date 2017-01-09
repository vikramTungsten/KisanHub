from django.conf.urls import include, url
from django.contrib import admin

from kisanhubapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'KisanHubProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/', views.data),
    url(r'^download/', views.download),
    url(r'^$', views.index),
]
