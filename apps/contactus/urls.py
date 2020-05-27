from django.urls import path
from apps.contactus import views
#import .views
#from blog.views import portfolio


urlpatterns = [
    # path('', views.portfolio_view, name='portfolio'),
    path('', views.ContactForm.as_view(), name='contactus'),
]