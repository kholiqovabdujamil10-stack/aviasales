from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('my-tickets/', my_tickets, name='my_tickets'),
    path('edit-ticket/<int:id>/', edit_ticket, name='edit_ticket'),
    path('delete-ticket/<int:id>/', delete_ticket, name='delete_ticket'),
]
