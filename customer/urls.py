from django.urls import path
from .views import home, save, edit, update, delete, user_register, user_login, logout_view

urlpatterns = [
    path('', home, name="home"),
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('logout/', logout_view, name='logout_view'),
    path('save/', save, name="save"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]