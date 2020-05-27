"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
# Below tow package for Media_URL
from django.conf import settings
from django.conf.urls.static import static

#===========Admin Panel Setting =====
admin.site.site_header = "MachineBlog Control Panel"
admin.site.site_title = "MachineBlog Control Panel"
admin.site.index_title = "MachineBlog Panel"


urlpatterns = [
   path('', include('apps.blog.urls')),
   path('portfolio/', include('apps.portfolio.urls')),
   path('contactus/', include('apps.contactus.urls')),
  
    #path('webapi/', include('webApi.urls')),
    path('cpanel/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
