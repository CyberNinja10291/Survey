from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_data/', views.all_data, name='all_data'),
    path('success-page/', views.success_page, name='success_page'),
    path('submit_data/', views.submit_data, name='submit_data'),
    path('user_data/<int:user_id>/', views.user_data, name='user_data'),
]
