from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.index , name = 'index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('all_user',views.all_user , name = 'all_user'),
    path('add_user',views.add_user , name = 'add_user'),
    path('bulk_upload',views.bulk_upload , name = 'bulk_upload'),
    path('update_user/<int:user_id>',views.update_user , name = 'update_user'),
    path('delete_user_id/<int:user_id>',views.delete_user_id , name = 'delete_user_id'),
    path('bulk_upload',views.bulk_upload , name = 'bulk_upload'),
    path('filter_user',views.filter_user , name = 'filter_user'),
    path('create_event/<int:user_id>',views.create_event , name = 'create_event'),

    path('view_profile/<int:user_id>',views.view_profile , name = 'view_profile'),

]