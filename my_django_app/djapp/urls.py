from django.urls import path 
from . import views

urlpatterns = [
    path('home/', views.home , name='home'),
    path('show/<st_id>', views.show , name='show'),
    path('delete/<st_id>', views.delete , name='delete'),
    path('add/', views.addStudent , name='add'),
    path('edit/<st_id>', views.edit , name='edit'),

    #rest_framework_path
    path('api-all/', views.api_all_student , name='api-all'),
    path('api-one/<st_id>', views.api_one_student , name='api-one'),
    path('api-add/', views.api_add_student , name='api-add'),
    path('api-edit/<st_id>', views.api_edit_student , name='api-edit'),
    path('api-delete/<st_id>', views.api_delete_student , name='api-delete'),
    path('login',views.loginPg , name='login'),
    path('signup',views.signupPg , name='signup'),
    path('signout',views.signoutPg , name='signout')
]