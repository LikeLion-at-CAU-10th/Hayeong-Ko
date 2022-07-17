from django.urls import path
from .views import *

urlpatterns = [
    path('create-profile/', create_profile, name="create_profile"),
    path('get-profile-all/', get_profile_all, name="get_profile_all"),
    path('get-profile-one/<int:id>', get_profile_one, name="get_profile_one"),
    path('update-profile/<int:id>', update_profile, name="update-profile"),
    path('delete-profile/<int:id>', delete_profile, name="delete-profile"),
    path('create-url/<int:profile_id>', create_url, name="create_url"),
    path('get-url/', get_url, name="get_url")
]