from . import views
from django.urls import path

# based on CI walkthrough blog project
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('actor_list/', views.ActorList.as_view(), name='actor_list'),
    path('actor/<int:id>/', views.ActorDetail.as_view(), name='actor_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
