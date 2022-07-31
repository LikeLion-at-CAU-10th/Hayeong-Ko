from django.urls import path
from .views import LikeLionCreateView, LikeLionDeleteView, LikeLionDetailView, LikeLionListView, LikeLionUpdateView

urlpatterns = [
    path('create/', LikeLionCreateView.as_view(), name="likelion_create"),
    path('list/', LikeLionListView.as_view(), name="likelion_list_all"),
    path('update/<int:pk>/', LikeLionUpdateView.as_view(), name="likelion_update"),
    path('delete/<int:pk>/', LikeLionDeleteView.as_view(), name="likelion_delete"),
    path('detail/<int:pk>/', LikeLionDetailView.as_view(), name='likelion_detail'),
]