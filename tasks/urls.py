from django.urls import path
from . import views, auth
urlpatterns =[
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create', views.add_task, name='create'),
    path('tasks/<int:pk>/delete_task', views.delete_task, name='delete_task'),
    path('tasks/<int:pk>/edit_task', views.edit_task, name='edit_task'),
    path('tasks/<int:pk>/done', views.done, name='done'),
    
    
    path('auth/signup', auth.signup, name='signup'),
    path('auth/login', auth.login_user, name='login'),
    path('auth/logout', auth.logout, name='logout'),
    
    
    
]
