from django.urls import path
from .views import *

urlpatterns = [
    path('create-category/', create_category, name="create_category"),
    path('get-category-all/', get_category_all, name="get_category_all"),
    path('get-category/<int:id>', get_category, name="get_category"),
    path('update-category/<int:id>', update_category, name='update-category'),
    path('delete-category/<int:id>', delete_category, name='delete-category'),
]
