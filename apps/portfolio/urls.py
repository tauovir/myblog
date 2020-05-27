from django.urls import path
from apps.portfolio import views
#import .views
#from blog.views import portfolio


urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
]